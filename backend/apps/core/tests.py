from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from django.urls import reverse
from datetime import date, time
from rest_framework import status
from rest_framework.test import APITestCase

from .models import (
    AcademicPeriod,
    AcademicProgram,
    Role,
    Subject,
    SubjectGroup,
    SubjectOffering,
    UserProfile,
    WorkingDay,
)
from .services.config_service import (
    ConfigValidationError,
    create_academic_period,
    create_space_type,
    create_time_slot,
    create_working_day,
    update_academic_period,
    update_space_type,
    update_time_slot,
    update_working_day,
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


class ProgrammingTests(BaseAuthTestCase):
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
        self.active_period = AcademicPeriod.objects.create(
            code="2026-1",
            name="Periodo 2026-1",
            start_date=date(2026, 1, 1),
            end_date=date(2026, 6, 30),
            is_active=True,
        )
        self.subject = Subject.objects.create(
            code="MAT101",
            name="Calculo I",
            class_type=Subject.CLASS_TYPE_PRESENCIAL,
            credits=3,
            weekly_hours=4,
            capacity=40,
            difficulty=160,
        )
        self.subject_group = SubjectGroup.objects.create(
            subject=self.subject,
            identifier="Grupo 1",
        )
        self.academic_program = AcademicProgram.objects.create(
            code="ING-SIS", name="Ingenieria de Sistemas"
        )

    def test_admin_can_create_subject_group(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subject-groups-list-create"),
            {
                "subject_id": self.subject.id,
                "identifier": "Grupo 2",
                "is_active": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["identifier"], "Grupo 2")

    def test_admin_can_create_subject_with_difficulty_calculated(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subjects-list-create"),
            {
                "code": "FIS101",
                "name": "Fisica I",
                "class_type": "virtual",
                "credits": 4,
                "weekly_hours": 5,
                "capacity": 35,
                "is_active": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["difficulty"], 175)

    def test_admin_can_update_subject_intensity_and_recalculate_difficulty(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.patch(
            reverse("programming-subjects-detail", kwargs={"config_id": self.subject.id}),
            {
                "weekly_hours": 6,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["difficulty"], 240)

    def test_subject_code_must_be_unique(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subjects-list-create"),
            {
                "code": "MAT101",
                "name": "Calculo I Duplicada",
                "class_type": "presencial",
                "credits": 3,
                "weekly_hours": 4,
                "capacity": 30,
                "is_active": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("code", response.data)

    def test_subject_numeric_fields_must_be_positive(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subjects-list-create"),
            {
                "code": "QUI101",
                "name": "Quimica I",
                "class_type": "virtual",
                "credits": 0,
                "weekly_hours": 0,
                "capacity": 0,
                "is_active": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("credits", response.data)

    def test_duplicate_subject_group_is_rejected(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subject-groups-list-create"),
            {
                "subject_id": self.subject.id,
                "identifier": "Grupo 1",
                "is_active": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("identifier", response.data)
        self.assertIn("Ya existe un grupo", str(response.data["identifier"][0]))

    def test_subject_offering_requires_semester(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subject-offerings-list-create"),
            {
                "subject_id": self.subject.id,
                "subject_group_id": self.subject_group.id,
                "academic_program_id": self.academic_program.id,
                "semester": "",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("semester", response.data)

    def test_subject_offering_is_assigned_to_active_period(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("programming-subject-offerings-list-create"),
            {
                "subject_id": self.subject.id,
                "subject_group_id": self.subject_group.id,
                "academic_program_id": self.academic_program.id,
                "semester": 3,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["academic_period"]["id"], self.active_period.id)
        self.assertEqual(response.data["semester"], 3)

    def test_subject_offering_rejects_duplicates_for_same_period(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        payload = {
            "subject_id": self.subject.id,
            "subject_group_id": self.subject_group.id,
            "academic_program_id": self.academic_program.id,
            "semester": 3,
        }

        first_response = self.client.post(
            reverse("programming-subject-offerings-list-create"), payload, format="json"
        )
        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)

        second_response = self.client.post(
            reverse("programming-subject-offerings-list-create"), payload, format="json"
        )
        self.assertEqual(second_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("subject_group_id", second_response.data)

    def test_coordinator_can_list_catalogs_for_programming(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")

        subjects_response = self.client.get(reverse("programming-subjects-list-create"))
        programs_response = self.client.get(reverse("programming-academic-programs-list-create"))

        self.assertEqual(subjects_response.status_code, status.HTTP_200_OK)
        self.assertEqual(programs_response.status_code, status.HTTP_200_OK)

    def test_coordinator_cannot_create_catalog_entries(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")

        subject_response = self.client.post(
            reverse("programming-subjects-list-create"),
            {"code": "FIS101", "name": "Fisica I", "is_active": True},
            format="json",
        )
        program_response = self.client.post(
            reverse("programming-academic-programs-list-create"),
            {"code": "ING-IND", "name": "Ingenieria Industrial", "is_active": True},
            format="json",
        )

        self.assertEqual(subject_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(program_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_coordinator_can_register_subject_offering(self):
        self.login_and_set_auth("coord@test.com", "coordpassword123")

        response = self.client.post(
            reverse("programming-subject-offerings-list-create"),
            {
                "subject_id": self.subject.id,
                "subject_group_id": self.subject_group.id,
                "academic_program_id": self.academic_program.id,
                "semester": 4,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["academic_period"]["id"], self.active_period.id)
        self.assertEqual(response.data["semester"], 4)


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

    def test_logout_requires_refresh_token(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(reverse("auth-logout"), {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("refresh token", str(response.data).lower())

    def test_logout_rejects_invalid_refresh_token(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        response = self.client.post(
            reverse("auth-logout"),
            {"refresh": "token-invalido"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("invalido", str(response.data).lower())

    def test_refresh_returns_new_access_token(self):
        login_response = self.client.post(
            reverse("auth-login"),
            {"email": "admin@test.com", "password": "adminpassword123"},
            format="json",
        )

        refresh_response = self.client.post(
            reverse("auth-refresh"),
            {"refresh": login_response.data["refresh"]},
            format="json",
        )

        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)

    def test_blacklisted_refresh_token_cannot_be_refreshed(self):
        login_response = self.client.post(
            reverse("auth-login"),
            {"email": "admin@test.com", "password": "adminpassword123"},
            format="json",
        )
        access_token = login_response.data["access"]
        refresh_token = login_response.data["refresh"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        logout_response = self.client.post(
            reverse("auth-logout"),
            {"refresh": refresh_token},
            format="json",
        )
        self.assertEqual(logout_response.status_code, status.HTTP_204_NO_CONTENT)

        refresh_response = self.client.post(
            reverse("auth-refresh"),
            {"refresh": refresh_token},
            format="json",
        )

        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_returns_profile_as_null_for_superuser_without_profile(self):
        superuser = User.objects.create_superuser(
            username="root@test.com",
            email="root@test.com",
            password="superpassword123",
        )

        login_response = self.client.post(
            reverse("auth-login"),
            {"email": "root@test.com", "password": "superpassword123"},
            format="json",
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {login_response.data['access']}")

        me_response = self.client.get(reverse("auth-me"))

        self.assertEqual(me_response.status_code, status.HTTP_200_OK)
        self.assertEqual(me_response.data["role"], "administrador")
        self.assertIsNone(me_response.data["profile"]["id"])
        self.assertIsNone(me_response.data["profile"]["is_active"])


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

    def test_admin_can_filter_users_by_role_status_and_search(self):
        docente_user = self.create_user(
            email="docente.filtro@test.com",
            password="docentepassword123",
            role=self.docente_role,
            first_name="Dora",
            last_name="Docente",
        )
        docente_user.profile.is_active = False
        docente_user.profile.save(update_fields=["is_active", "updated_at"])

        self.login_and_set_auth("admin@test.com", "adminpassword123")

        role_filtered = self.client.get(
            reverse("users-list-create"),
            {"role_id": self.coordinator_role.id},
        )
        self.assertEqual(role_filtered.status_code, status.HTTP_200_OK)
        self.assertTrue(all(item["role"]["name"] == "Coordinador" for item in role_filtered.data))

        active_filtered = self.client.get(
            reverse("users-list-create"),
            {"is_active": "false"},
        )
        self.assertEqual(active_filtered.status_code, status.HTTP_200_OK)
        self.assertTrue(all(item["is_active"] is False for item in active_filtered.data))

        search_filtered = self.client.get(
            reverse("users-list-create"),
            {"search": "Carlos"},
        )
        self.assertEqual(search_filtered.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Carlos" in item["first_name"] for item in search_filtered.data))

    def test_invalid_is_active_filter_is_ignored(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        baseline = self.client.get(reverse("users-list-create"))
        filtered = self.client.get(reverse("users-list-create"), {"is_active": "talvez"})

        self.assertEqual(baseline.status_code, status.HTTP_200_OK)
        self.assertEqual(filtered.status_code, status.HTTP_200_OK)
        self.assertEqual(len(filtered.data), len(baseline.data))


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

    def test_admin_can_list_each_config_resource(self):
        self.login_and_set_auth("admin@test.com", "adminpassword123")

        self.client.post(
            reverse("config-periods-list-create"),
            {
                "code": "2026-L",
                "name": "Periodo listado",
                "start_date": "2026-01-10",
                "end_date": "2026-05-20",
            },
            format="json",
        )
        self.client.post(
            reverse("config-working-days-list-create"),
            {"day_of_week": 2, "name": "Martes"},
            format="json",
        )
        self.client.post(
            reverse("config-time-slots-list-create"),
            {"name": "Franja listada", "start_time": "08:00:00", "end_time": "09:00:00"},
            format="json",
        )
        self.client.post(
            reverse("config-space-types-list-create"),
            {"name": "Aula", "description": "Tipo aula"},
            format="json",
        )

        periods_response = self.client.get(reverse("config-periods-list-create"))
        days_response = self.client.get(reverse("config-working-days-list-create"))
        slots_response = self.client.get(reverse("config-time-slots-list-create"))
        types_response = self.client.get(reverse("config-space-types-list-create"))

        self.assertEqual(periods_response.status_code, status.HTTP_200_OK)
        self.assertEqual(days_response.status_code, status.HTTP_200_OK)
        self.assertEqual(slots_response.status_code, status.HTTP_200_OK)
        self.assertEqual(types_response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(periods_response.data), 1)
        self.assertGreaterEqual(len(days_response.data), 1)
        self.assertGreaterEqual(len(slots_response.data), 1)
        self.assertGreaterEqual(len(types_response.data), 1)


class PermissionUtilityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_role, _ = Role.objects.get_or_create(name="Administrador")

    def test_get_user_role_name_returns_none_for_anonymous(self):
        from .permissions import get_user_role_name

        self.assertIsNone(get_user_role_name(AnonymousUser()))

    def test_get_user_role_name_returns_none_when_profile_is_missing(self):
        from .permissions import get_user_role_name

        user = User.objects.create_user(
            username="sinperfil@test.com",
            email="sinperfil@test.com",
            password="password12345",
        )

        self.assertIsNone(get_user_role_name(user))

    def test_has_allowed_roles_without_configured_roles_returns_true(self):
        from .permissions import HasAllowedRoles

        user = User.objects.create_user(
            username="noperfiltwo@test.com",
            email="noperfiltwo@test.com",
            password="password12345",
        )

        request = type("Request", (), {"user": user})
        view = type("View", (), {})

        permission = HasAllowedRoles()
        self.assertTrue(permission.has_permission(request, view))


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

    def test_period_update_and_duplicate_code_validation(self):
        first = create_academic_period(
            code="2026-1",
            name="Periodo 1",
            start_date=date(2026, 1, 10),
            end_date=date(2026, 5, 30),
            is_active=True,
        )
        second = create_academic_period(
            code="2026-2",
            name="Periodo 2",
            start_date=date(2026, 7, 1),
            end_date=date(2026, 11, 30),
            is_active=True,
        )

        updated = update_academic_period(
            first,
            code="2026-1A",
            name="Periodo 1A",
            start_date=date(2026, 1, 15),
            end_date=date(2026, 6, 1),
            is_active=False,
        )

        self.assertEqual(updated.code, "2026-1A")
        self.assertFalse(updated.is_active)

        with self.assertRaises(ConfigValidationError):
            update_academic_period(
                second,
                code="2026-1A",
                name="Duplicado",
                start_date=date(2026, 7, 1),
                end_date=date(2026, 11, 30),
                is_active=True,
            )

    def test_working_day_update_and_duplicate_validation(self):
        monday = create_working_day(day_of_week=1, name="Lunes", is_active=True)
        tuesday = create_working_day(day_of_week=2, name="Martes", is_active=True)

        updated = update_working_day(
            monday,
            day_of_week=3,
            name="Miercoles",
            is_active=False,
        )
        self.assertEqual(updated.day_of_week, 3)
        self.assertFalse(updated.is_active)

        with self.assertRaises(ConfigValidationError):
            update_working_day(
                tuesday,
                day_of_week=3,
                name="Martes",
                is_active=True,
            )

    def test_time_slot_duplicate_validation(self):
        create_time_slot(
            name="Franja",
            start_time=time(7, 0),
            end_time=time(8, 0),
            is_active=True,
        )

        with self.assertRaises(ConfigValidationError):
            create_time_slot(
                name="Franja",
                start_time=time(7, 0),
                end_time=time(8, 0),
                is_active=True,
            )

    def test_space_type_update_and_duplicate_validation(self):
        lab = create_space_type(name="Laboratorio", description="Lab", is_active=True)
        aula = create_space_type(name="Aula", description="Clase", is_active=True)

        updated = update_space_type(
            lab,
            name="Laboratorio Avanzado",
            description="Lab de hardware",
            is_active=False,
        )
        self.assertEqual(updated.name, "Laboratorio Avanzado")
        self.assertFalse(updated.is_active)

        with self.assertRaises(ConfigValidationError):
            update_space_type(
                aula,
                name="Laboratorio Avanzado",
                description="Duplicado",
                is_active=True,
            )
