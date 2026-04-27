from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    AcademicPeriod,
    AcademicProgram,
    Role,
    SpaceType,
    Subject,
    SubjectGroup,
    SubjectOffering,
    TimeSlot,
    UserProfile,
    WorkingDay,
)
from .services.health_service import build_health_payload
from .permissions import HasAllowedRoles, get_user_role_name
from .serializers import (
    LoginSerializer,
    RoleSerializer,
    AcademicPeriodSerializer,
    AcademicProgramSerializer,
    SpaceTypeSerializer,
    SubjectGroupSerializer,
    SubjectOfferingSerializer,
    SubjectSerializer,
    TimeSlotSerializer,
    UserCreateSerializer,
    UserProfileReadSerializer,
    UserUpdateSerializer,
    WorkingDaySerializer,
)
from .services.user_service import deactivate_user_profile
from .services.programming_service import get_active_academic_period


@api_view(["GET"])
def health_check(_request):
    return Response(build_health_payload())


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            raise ValidationError("Se requiere el refresh token para cerrar sesion.")

        try:
            RefreshToken(refresh_token).blacklist()
        except TokenError as exc:
            raise ValidationError("Refresh token invalido o expirado.") from exc

        return Response(status=204)


class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role_name = get_user_role_name(request.user)
        profile = getattr(request.user, "profile", None)

        return Response(
            {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "role": role_name,
                "is_superuser": request.user.is_superuser,
                "profile": {
                    "id": profile.id if profile else None,
                    "is_active": profile.is_active if profile else None,
                },
            }
        )


class AdminOnlyAPIView(APIView):
    permission_classes = [IsAuthenticated, HasAllowedRoles]
    allowed_roles = ("administrador",)

    def get(self, request):
        return Response(
            {
                "message": "Acceso validado para administradores.",
                "role": get_user_role_name(request.user),
            }
        )


class AdminProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated, HasAllowedRoles]
    allowed_roles = ("administrador",)


class CoordinatorProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated, HasAllowedRoles]
    allowed_roles = ("administrador", "coordinador")


class RoleListAPIView(AdminProtectedAPIView):
    def get(self, _request):
        queryset = Role.objects.filter(is_active=True).order_by("name")
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)


class UserListCreateAPIView(AdminProtectedAPIView):
    def get(self, request):
        queryset = UserProfile.objects.select_related("role", "user").order_by(
            "last_name", "first_name"
        )

        role_id = request.query_params.get("role_id")
        is_active = request.query_params.get("is_active")
        search = request.query_params.get("search")

        if role_id:
            queryset = queryset.filter(role_id=role_id)

        if is_active is not None:
            normalized_value = is_active.strip().lower()
            if normalized_value in ("true", "1"):
                queryset = queryset.filter(is_active=True)
            elif normalized_value in ("false", "0"):
                queryset = queryset.filter(is_active=False)

        if search:
            queryset = queryset.filter(
                Q(email__icontains=search)
                | Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
            )

        serializer = UserProfileReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        response_serializer = UserProfileReadSerializer(profile)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class UserDetailAPIView(AdminProtectedAPIView):
    def get_object(self, user_profile_id):
        return get_object_or_404(
            UserProfile.objects.select_related("role", "user"),
            id=user_profile_id,
        )

    def patch(self, request, user_profile_id):
        profile = self.get_object(user_profile_id)
        serializer = UserUpdateSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_profile = serializer.save()
        response_serializer = UserProfileReadSerializer(updated_profile)
        return Response(response_serializer.data)

    def delete(self, _request, user_profile_id):
        profile = self.get_object(user_profile_id)
        deactivate_user_profile(profile)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConfigListCreateBaseAPIView(AdminProtectedAPIView):
    queryset = None
    serializer_class = None

    def get(self, _request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        response_serializer = self.serializer_class(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class ConfigDetailBaseAPIView(AdminProtectedAPIView):
    queryset = None
    serializer_class = None

    def get_object(self, config_id):
        return get_object_or_404(self.queryset, id=config_id)

    def patch(self, request, config_id):
        instance = self.get_object(config_id)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        response_serializer = self.serializer_class(updated_instance)
        return Response(response_serializer.data)

    def delete(self, _request, config_id):
        instance = self.get_object(config_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoordinatorReadableConfigListCreateAPIView(CoordinatorProtectedAPIView):
    queryset = None
    serializer_class = None

    def get(self, _request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        if get_user_role_name(request.user) != "administrador":
            raise PermissionDenied("Solo administradores pueden crear en este catalogo.")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        response_serializer = self.serializer_class(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class AcademicPeriodListCreateAPIView(ConfigListCreateBaseAPIView):
    queryset = AcademicPeriod.objects.order_by("-start_date")
    serializer_class = AcademicPeriodSerializer


class AcademicPeriodDetailAPIView(ConfigDetailBaseAPIView):
    queryset = AcademicPeriod.objects.all()
    serializer_class = AcademicPeriodSerializer


class WorkingDayListCreateAPIView(ConfigListCreateBaseAPIView):
    queryset = WorkingDay.objects.order_by("day_of_week")
    serializer_class = WorkingDaySerializer


class WorkingDayDetailAPIView(ConfigDetailBaseAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class TimeSlotListCreateAPIView(ConfigListCreateBaseAPIView):
    queryset = TimeSlot.objects.order_by("start_time")
    serializer_class = TimeSlotSerializer


class TimeSlotDetailAPIView(ConfigDetailBaseAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class SpaceTypeListCreateAPIView(ConfigListCreateBaseAPIView):
    queryset = SpaceType.objects.order_by("name")
    serializer_class = SpaceTypeSerializer


class SpaceTypeDetailAPIView(ConfigDetailBaseAPIView):
    queryset = SpaceType.objects.all()
    serializer_class = SpaceTypeSerializer


class AcademicProgramListCreateAPIView(CoordinatorReadableConfigListCreateAPIView):
    queryset = AcademicProgram.objects.order_by("code")
    serializer_class = AcademicProgramSerializer


class AcademicProgramDetailAPIView(ConfigDetailBaseAPIView):
    queryset = AcademicProgram.objects.all()
    serializer_class = AcademicProgramSerializer


class SubjectListCreateAPIView(CoordinatorReadableConfigListCreateAPIView):
    queryset = Subject.objects.order_by("code")
    serializer_class = SubjectSerializer


class SubjectDetailAPIView(ConfigDetailBaseAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectGroupListCreateAPIView(CoordinatorReadableConfigListCreateAPIView):
    queryset = SubjectGroup.objects.select_related("subject").order_by("subject__code", "identifier")
    serializer_class = SubjectGroupSerializer


class SubjectGroupDetailAPIView(ConfigDetailBaseAPIView):
    queryset = SubjectGroup.objects.select_related("subject").all()
    serializer_class = SubjectGroupSerializer


class SubjectOfferingListCreateAPIView(CoordinatorProtectedAPIView):
    def get(self, _request):
        active_period = get_active_academic_period()
        if active_period is None:
            queryset = SubjectOffering.objects.none()
        else:
            queryset = SubjectOffering.objects.select_related(
                "subject", "academic_program", "academic_period"
            ).filter(academic_period=active_period).order_by("semester", "subject__code")

        serializer = SubjectOfferingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectOfferingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        response_serializer = SubjectOfferingSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class SubjectOfferingDetailAPIView(CoordinatorProtectedAPIView):
    def get_object(self, subject_offering_id):
        return get_object_or_404(
            SubjectOffering.objects.select_related("subject", "academic_program", "academic_period"),
            id=subject_offering_id,
        )

    def patch(self, request, subject_offering_id):
        instance = self.get_object(subject_offering_id)
        serializer = SubjectOfferingSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        response_serializer = SubjectOfferingSerializer(updated_instance)
        return Response(response_serializer.data)

    def delete(self, _request, subject_offering_id):
        instance = self.get_object(subject_offering_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
