from django.contrib import admin

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


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ("name", "is_active", "created_at", "updated_at")
	search_fields = ("name",)
	list_filter = ("is_active",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "email", "first_name", "last_name", "role", "is_active")
	search_fields = ("user__username", "email", "first_name", "last_name")
	list_filter = ("role", "is_active")


@admin.register(AcademicPeriod)
class AcademicPeriodAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "start_date", "end_date", "is_active")
	search_fields = ("code", "name")
	list_filter = ("is_active",)


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "is_active", "created_at", "updated_at")
	search_fields = ("code", "name")
	list_filter = ("is_active",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = (
		"code",
		"name",
		"class_type",
		"credits",
		"weekly_hours",
		"capacity",
		"difficulty",
		"is_active",
		"created_at",
		"updated_at",
	)
	search_fields = ("code", "name")
	list_filter = ("is_active", "class_type")


@admin.register(SubjectGroup)
class SubjectGroupAdmin(admin.ModelAdmin):
	list_display = ("subject", "identifier", "is_active", "created_at", "updated_at")
	search_fields = ("subject__code", "identifier")
	list_filter = ("is_active", "subject")


@admin.register(SubjectOffering)
class SubjectOfferingAdmin(admin.ModelAdmin):
	list_display = (
		"subject",
		"subject_group",
		"academic_program",
		"academic_period",
		"semester",
		"is_active",
	)
	search_fields = (
		"subject__code",
		"subject_group__identifier",
		"academic_program__code",
		"academic_period__code",
	)
	list_filter = ("is_active", "academic_period", "academic_program")


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
	list_display = ("name", "start_time", "end_time", "is_active")
	search_fields = ("name",)
	list_filter = ("is_active",)


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
	list_display = ("day_of_week", "name", "is_active")
	search_fields = ("name",)
	list_filter = ("is_active",)


@admin.register(SpaceType)
class SpaceTypeAdmin(admin.ModelAdmin):
	list_display = ("name", "is_active", "created_at", "updated_at")
	search_fields = ("name",)
	list_filter = ("is_active",)
