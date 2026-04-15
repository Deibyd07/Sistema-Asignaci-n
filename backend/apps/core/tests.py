from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from datetime import date, time
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Role, UserProfile, WorkingDay
from .services.config_service import (
    ConfigValidationError,
    create_academic_period,
    create_time_slot,
    create_working_day,
    update_time_slot,
)
from .services.user_service import (
    UserEmailAlreadyExistsError,
    create_user_with_profile,
    deactivate_user_profile,
    update_user_profile,
)


class BaseAuthTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_role, _ = Role.objects.get_or_create(name="Administrador")
        cls.coordinator_role, _ = Role.objects.get_or_create(name="Coordinador")
        cls.docente_role, _ = Role.objects.get_or_create(name="Docente")
        cls.estudiante_role, _ = Role.objects.get_or_create(name="Estudiante")

    def create_user(self, email, password, role, first_name, last_name):
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        UserProfile.objects.create(
            user=user,
            role=role,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        return user

    def login_and_set_auth(self, email, password):
        login_response = self.client.post(
            reverse("auth-login"),
            {"email": email, "password": password},
            format="json",
        )
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        return login_response


class HealthCheckTests(APITestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")


class AuthenticationTests(BaseAuthTestCase):
    def setUp(self):
        self.admin_user = self.create_user(
            email="admin@test.com",
            password="adminpassword123",
            role=self.admin_role,
            first_name="Ana",
            last_name="Admin",
        )
        self.coordinator_user = self.create_user(
            email="coord@test.com",
            password="coordpassword123",
            role=self.coordinator_role,
            first_name="Carlos",
            last_name="Coord",
        )

    def test_login_returns_tokens_and_user_data(self):
        response = self.client.post(
            reverse("auth-login"),
            {"email": "admin@test.com", "password": "adminpassword123"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["user"]["email"], "admin@test.com")
        self.assertEqual(response.data["user"]["role"], "administrador")

    def test_login_rejects_invalid_credentials(self):
        response = self.client.post(
            reverse("auth-login"),
            {"email": "admin@test.com", "password": "wrong-password"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Credenciales invalidas", str(response.data))

    def test_me_returns_authenticated_user(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")
        response = self.client.get(reverse("auth-me"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "admin@test.com")
        self.assertEqual(response.data["role"], "administrador")

    def test_admin_only_allows_admin_role(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")
        response = self.client.get(reverse("auth-admin-only"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["role"], "administrador")

    def test_admin_only_denies_coordinator_role(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")
        response = self.client.get(reverse("auth-admin-only"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logout_blacklists_refresh_token(self):
        login_response = self.client.post(
            reverse("auth-login"),
            {"email": "admin@test.com", "password": "adminpassword123"},
            format="json",
        )
        access_token = login_response.data["access"]
        refresh_token = login_response.data["refresh"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.post(
            reverse("auth-logout"),
            {"refresh": refresh_token},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UserManagementApiTests(BaseAuthTestCase):
    def setUp(self):
        self.admin_user = self.create_user(
            email="admin@test.com",
            password="adminpassword123",
            role=self.admin_role,
            first_name="Ana",
            last_name="Admin",
        )
        self.coordinator_user = self.create_user(
            email="coord@test.com",
            password="coordpassword123",
            role=self.coordinator_role,
            first_name="Carlos",
            last_name="Coord",
        )

    def test_admin_can_create_user(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("users-list-create"),
            {
                "email": "docente@test.com",
                "password": "docentepassword123",
                "first_name": "Diana",
                "last_name": "Docente",
                "role_id": self.docente_role.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "docente@test.com")
        self.assertEqual(response.data["role"]["name"], "Docente")

    def test_non_admin_cannot_create_user(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")

        response = self.client.post(
            reverse("users-list-create"),
            {
                "email": "nuevo@test.com",
                "password": "nuevopassword123",
                "first_name": "Nuevo",
                "last_name": "Usuario",
                "role_id": self.estudiante_role.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_email_must_be_unique(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("users-list-create"),
            {
                "email": "coord@test.com",
                "password": "nuevopassword123",
                "first_name": "Duplicado",
                "last_name": "Correo",
                "role_id": self.estudiante_role.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_admin_can_edit_user_role(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        coordinator_profile = self.coordinator_user.profile
        response = self.client.patch(
            reverse("users-detail", kwargs={"user_profile_id": coordinator_profile.id}),
            {"role_id": self.docente_role.id},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["role"]["name"], "Docente")

    def test_admin_can_deactivate_user(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        coordinator_profile = self.coordinator_user.profile
        response = self.client.delete(
            reverse("users-detail", kwargs={"user_profile_id": coordinator_profile.id})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        coordinator_profile.refresh_from_db()
        self.coordinator_user.refresh_from_db()
        self.assertFalse(coordinator_profile.is_active)
        self.assertFalse(self.coordinator_user.is_active)

    def test_roles_endpoint_returns_minimum_required_roles(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.get(reverse("roles-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        role_names = {item["name"] for item in response.data}
        self.assertTrue({"Administrador", "Coordinador", "Docente", "Estudiante"}.issubset(role_names))

    def test_role_change_applies_without_relogin(self):
        coordinator_login = self.client.post(
            reverse("auth-login"),
            {"email": "coord@test.com", "password": "coordpassword123"},
            format="json",
        )
        coordinator_token = coordinator_login.data["access"]

        self.login_and_set_auth("admin@test.com", "adminpassword123")
        self.client.patch(
            reverse("users-detail", kwargs={"user_profile_id": self.coordinator_user.profile.id}),
            {"role_id": self.docente_role.id},
            format="json",
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {coordinator_token}")
        me_response = self.client.get(reverse("auth-me"))

        self.assertEqual(me_response.status_code, status.HTTP_200_OK)
        self.assertEqual(me_response.data["role"], "docente")


class UserServiceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_role, _ = Role.objects.get_or_create(name="Administrador")
        cls.coordinator_role, _ = Role.objects.get_or_create(name="Coordinador")

    def test_create_user_with_profile(self):
        profile = create_user_with_profile(
            email="servicio@test.com",
            password="serviciopassword123",
            first_name="Sofia",
            last_name="Servicio",
            role=self.admin_role,
        )

        self.assertEqual(profile.email, "servicio@test.com")
        self.assertEqual(profile.user.username, "servicio@test.com")
        self.assertEqual(profile.role.name, "Administrador")

    def test_create_user_rejects_duplicate_email(self):
        create_user_with_profile(
            email="duplicado@test.com",
            password="serviciopassword123",
            first_name="Primero",
            last_name="Usuario",
            role=self.admin_role,
        )

        with self.assertRaises(UserEmailAlreadyExistsError):
            create_user_with_profile(
                email="duplicado@test.com",
                password="serviciopassword123",
                first_name="Segundo",
                last_name="Usuario",
                role=self.coordinator_role,
            )

    def test_update_user_profile(self):
        profile = create_user_with_profile(
            email="update@test.com",
            password="serviciopassword123",
            first_name="Original",
            last_name="Nombre",
            role=self.admin_role,
        )

        updated_profile = update_user_profile(
            profile,
            email="actualizado@test.com",
            first_name="Actualizado",
            last_name="Usuario",
            role=self.coordinator_role,
            is_active=True,
        )

        self.assertEqual(updated_profile.email, "actualizado@test.com")
        self.assertEqual(updated_profile.user.email, "actualizado@test.com")
        self.assertEqual(updated_profile.role.name, "Coordinador")

    def test_deactivate_user_profile(self):
        profile = create_user_with_profile(
            email="desactivar@test.com",
            password="serviciopassword123",
            first_name="Des",
            last_name="Activar",
            role=self.admin_role,
        )

        deactivate_user_profile(profile)
        profile.refresh_from_db()
        profile.user.refresh_from_db()

        self.assertFalse(profile.is_active)
        self.assertFalse(profile.user.is_active)


class SystemConfigApiTests(BaseAuthTestCase):
    def setUp(self):
        self.admin_user = self.create_user(
            email="admin@test.com",
            password="adminpassword123",
            role=self.admin_role,
            first_name="Ana",
            last_name="Admin",
        )
        self.coordinator_user = self.create_user(
            email="coord@test.com",
            password="coordpassword123",
            role=self.coordinator_role,
            first_name="Carlos",
            last_name="Coord",
        )

    def test_admin_can_crud_academic_period(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        create_response = self.client.post(
            reverse("config-periods-list-create"),
            {
                "code": "2026-1",
                "name": "Periodo 2026-1",
                "start_date": "2026-01-15",
                "end_date": "2026-06-15",
                "is_active": True,
            },
            format="json",
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        period_id = create_response.data["id"]

        update_response = self.client.patch(
            reverse("config-periods-detail", kwargs={"config_id": period_id}),
            {"name": "Periodo 2026-A"},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["name"], "Periodo 2026-A")

        delete_response = self.client.delete(
            reverse("config-periods-detail", kwargs={"config_id": period_id})
        )
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_period_range_is_rejected(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("config-periods-list-create"),
            {
                "code": "2026-X",
                "name": "Periodo invalido",
                "start_date": "2026-08-01",
                "end_date": "2026-06-01",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("end_date", response.data)

    def test_invalid_timeslot_range_is_rejected(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("config-time-slots-list-create"),
            {
                "name": "Franja invalida",
                "start_time": "10:00:00",
                "end_time": "09:00:00",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("end_time", response.data)

    def test_admin_can_crud_working_day(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        create_response = self.client.post(
            reverse("config-working-days-list-create"),
            {"day_of_week": 1, "name": "Lunes", "is_active": True},
            format="json",
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        day_id = create_response.data["id"]

        update_response = self.client.patch(
            reverse("config-working-days-detail", kwargs={"config_id": day_id}),
            {"name": "Lunes Academico"},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["name"], "Lunes Academico")

        delete_response = self.client.delete(
            reverse("config-working-days-detail", kwargs={"config_id": day_id})
        )
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_admin_can_crud_time_slot_and_space_type(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        create_slot = self.client.post(
            reverse("config-time-slots-list-create"),
            {
                "name": "Franja 1",
                "start_time": "07:00:00",
                "end_time": "09:00:00",
                "is_active": True,
            },
            format="json",
        )
        self.assertEqual(create_slot.status_code, status.HTTP_201_CREATED)

        create_space = self.client.post(
            reverse("config-space-types-list-create"),
            {"name": "Laboratorio", "description": "Tipo laboratorio", "is_active": True},
            format="json",
        )
        self.assertEqual(create_space.status_code, status.HTTP_201_CREATED)

    def test_non_admin_cannot_manage_config(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")

        response = self.client.post(
            reverse("config-space-types-list-create"),
            {"name": "Auditorio", "description": "Tipo auditorio", "is_active": True},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ConfigServiceTests(TestCase):
    def test_create_period_validates_dates(self):
        with self.assertRaises(ConfigValidationError):
            create_academic_period(
                code="2026-2",
                name="Periodo invalido",
                start_date=date(2026, 7, 1),
                end_date=date(2026, 6, 1),
                is_active=True,
            )

    def test_create_working_day_validates_range(self):
        with self.assertRaises(ConfigValidationError):
            create_working_day(day_of_week=9, name="Fuera de rango", is_active=True)

    def test_create_and_update_time_slot_validate_range(self):
        with self.assertRaises(ConfigValidationError):
            create_time_slot(
                name="No valida",
                start_time=time(11, 0),
                end_time=time(10, 0),
                is_active=True,
            )

        valid_slot = create_time_slot(
            name="Valida",
            start_time=time(8, 0),
            end_time=time(10, 0),
            is_active=True,
        )

        with self.assertRaises(ConfigValidationError):
            update_time_slot(
                valid_slot,
                name="Valida",
                start_time=time(10, 0),
                end_time=time(10, 0),
                is_active=True,
            )

    def test_create_working_day_persists_data(self):
        day = create_working_day(day_of_week=2, name="Martes", is_active=True)

        self.assertEqual(day.day_of_week, 2)
        self.assertEqual(day.name, "Martes")
        self.assertTrue(WorkingDay.objects.filter(id=day.id).exists())
