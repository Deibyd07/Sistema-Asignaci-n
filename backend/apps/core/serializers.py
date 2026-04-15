from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import AcademicPeriod, Role, SpaceType, TimeSlot, UserProfile, WorkingDay
from .permissions import get_user_role_name
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
    update_user_profile,
)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        request = self.context.get("request")
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=request, username=email, password=password)
        if user is None:
            raise serializers.ValidationError("Credenciales invalidas.")

        refresh = RefreshToken.for_user(user)
        role_name = get_user_role_name(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": role_name,
                "is_superuser": user.is_superuser,
            },
        }


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name", "description", "is_active"]


class UserProfileReadSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user_id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "role",
            "created_at",
            "updated_at",
        ]


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8, trim_whitespace=False)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    role_id = serializers.PrimaryKeyRelatedField(source="role", queryset=Role.objects.all())

    def create(self, validated_data):
        try:
            return create_user_with_profile(**validated_data)
        except UserEmailAlreadyExistsError as exc:
            raise serializers.ValidationError({"email": str(exc)}) from exc


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    role_id = serializers.PrimaryKeyRelatedField(
        source="role", queryset=Role.objects.all(), required=False
    )
    is_active = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        payload = {
            "email": validated_data.get("email", instance.email),
            "first_name": validated_data.get("first_name", instance.first_name),
            "last_name": validated_data.get("last_name", instance.last_name),
            "role": validated_data.get("role", instance.role),
            "is_active": validated_data.get("is_active", instance.is_active),
        }

        try:
            return update_user_profile(instance, **payload)
        except UserEmailAlreadyExistsError as exc:
            raise serializers.ValidationError({"email": str(exc)}) from exc


class AcademicPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPeriod
        fields = ["id", "code", "name", "start_date", "end_date", "is_active"]

    def create(self, validated_data):
        try:
            return create_academic_period(**validated_data)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"end_date": str(exc)}) from exc

    def update(self, instance, validated_data):
        payload = {
            "code": validated_data.get("code", instance.code),
            "name": validated_data.get("name", instance.name),
            "start_date": validated_data.get("start_date", instance.start_date),
            "end_date": validated_data.get("end_date", instance.end_date),
            "is_active": validated_data.get("is_active", instance.is_active),
        }

        try:
            return update_academic_period(instance, **payload)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"end_date": str(exc)}) from exc


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ["id", "day_of_week", "name", "is_active"]

    def create(self, validated_data):
        try:
            return create_working_day(**validated_data)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"day_of_week": str(exc)}) from exc

    def update(self, instance, validated_data):
        payload = {
            "day_of_week": validated_data.get("day_of_week", instance.day_of_week),
            "name": validated_data.get("name", instance.name),
            "is_active": validated_data.get("is_active", instance.is_active),
        }

        try:
            return update_working_day(instance, **payload)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"day_of_week": str(exc)}) from exc


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ["id", "name", "start_time", "end_time", "is_active"]

    def create(self, validated_data):
        try:
            return create_time_slot(**validated_data)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"end_time": str(exc)}) from exc

    def update(self, instance, validated_data):
        payload = {
            "name": validated_data.get("name", instance.name),
            "start_time": validated_data.get("start_time", instance.start_time),
            "end_time": validated_data.get("end_time", instance.end_time),
            "is_active": validated_data.get("is_active", instance.is_active),
        }

        try:
            return update_time_slot(instance, **payload)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"end_time": str(exc)}) from exc


class SpaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceType
        fields = ["id", "name", "description", "is_active"]

    def create(self, validated_data):
        try:
            return create_space_type(**validated_data)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"name": str(exc)}) from exc

    def update(self, instance, validated_data):
        payload = {
            "name": validated_data.get("name", instance.name),
            "description": validated_data.get("description", instance.description),
            "is_active": validated_data.get("is_active", instance.is_active),
        }

        try:
            return update_space_type(instance, **payload)
        except ConfigValidationError as exc:
            raise serializers.ValidationError({"name": str(exc)}) from exc
