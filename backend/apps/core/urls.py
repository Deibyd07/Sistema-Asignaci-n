from django.urls import path

from .views import (
    AdminOnlyAPIView,
    AcademicPeriodDetailAPIView,
    AcademicPeriodListCreateAPIView,
    LoginAPIView,
    LogoutAPIView,
    MeAPIView,
    RoleListAPIView,
    SpaceTypeDetailAPIView,
    SpaceTypeListCreateAPIView,
    TimeSlotDetailAPIView,
    TimeSlotListCreateAPIView,
    UserDetailAPIView,
    UserListCreateAPIView,
    WorkingDayDetailAPIView,
    WorkingDayListCreateAPIView,
    health_check,
)

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("auth/login/", LoginAPIView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutAPIView.as_view(), name="auth-logout"),
    path("auth/me/", MeAPIView.as_view(), name="auth-me"),
    path("auth/admin-only/", AdminOnlyAPIView.as_view(), name="auth-admin-only"),
    path("roles/", RoleListAPIView.as_view(), name="roles-list"),
    path("users/", UserListCreateAPIView.as_view(), name="users-list-create"),
    path("users/<int:user_profile_id>/", UserDetailAPIView.as_view(), name="users-detail"),
    path(
        "config/periods/",
        AcademicPeriodListCreateAPIView.as_view(),
        name="config-periods-list-create",
    ),
    path(
        "config/periods/<int:config_id>/",
        AcademicPeriodDetailAPIView.as_view(),
        name="config-periods-detail",
    ),
    path(
        "config/working-days/",
        WorkingDayListCreateAPIView.as_view(),
        name="config-working-days-list-create",
    ),
    path(
        "config/working-days/<int:config_id>/",
        WorkingDayDetailAPIView.as_view(),
        name="config-working-days-detail",
    ),
    path(
        "config/time-slots/",
        TimeSlotListCreateAPIView.as_view(),
        name="config-time-slots-list-create",
    ),
    path(
        "config/time-slots/<int:config_id>/",
        TimeSlotDetailAPIView.as_view(),
        name="config-time-slots-detail",
    ),
    path(
        "config/space-types/",
        SpaceTypeListCreateAPIView.as_view(),
        name="config-space-types-list-create",
    ),
    path(
        "config/space-types/<int:config_id>/",
        SpaceTypeDetailAPIView.as_view(),
        name="config-space-types-detail",
    ),
]
