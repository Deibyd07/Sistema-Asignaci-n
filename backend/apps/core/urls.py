from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    AdminOnlyAPIView,
    AcademicPeriodDetailAPIView,
    AcademicPeriodListCreateAPIView,
    AcademicProgramDetailAPIView,
    AcademicProgramListCreateAPIView,
    LoginAPIView,
    LogoutAPIView,
    MeAPIView,
    RoleListAPIView,
    SpaceTypeDetailAPIView,
    SpaceTypeListCreateAPIView,
    SubjectDetailAPIView,
    SubjectListCreateAPIView,
    SubjectGroupDetailAPIView,
    SubjectGroupListCreateAPIView,
    SubjectOfferingDetailAPIView,
    SubjectOfferingListCreateAPIView,
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
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
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
    path(
        "programming/academic-programs/",
        AcademicProgramListCreateAPIView.as_view(),
        name="programming-academic-programs-list-create",
    ),
    path(
        "programming/academic-programs/<int:config_id>/",
        AcademicProgramDetailAPIView.as_view(),
        name="programming-academic-programs-detail",
    ),
    path(
        "programming/subjects/",
        SubjectListCreateAPIView.as_view(),
        name="programming-subjects-list-create",
    ),
    path(
        "programming/subjects/<int:config_id>/",
        SubjectDetailAPIView.as_view(),
        name="programming-subjects-detail",
    ),
    path(
        "programming/subject-groups/",
        SubjectGroupListCreateAPIView.as_view(),
        name="programming-subject-groups-list-create",
    ),
    path(
        "programming/subject-groups/<int:config_id>/",
        SubjectGroupDetailAPIView.as_view(),
        name="programming-subject-groups-detail",
    ),
    path(
        "programming/subject-offerings/",
        SubjectOfferingListCreateAPIView.as_view(),
        name="programming-subject-offerings-list-create",
    ),
    path(
        "programming/subject-offerings/<int:subject_offering_id>/",
        SubjectOfferingDetailAPIView.as_view(),
        name="programming-subject-offerings-detail",
    ),
]
