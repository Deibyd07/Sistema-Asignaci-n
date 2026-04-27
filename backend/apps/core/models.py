from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="users")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()


class AcademicPeriod(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_date__gte=models.F("start_date")),
                name="period_end_after_or_equal_start",
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"


class AcademicProgram(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Subject(TimeStampedModel):
    CLASS_TYPE_PRESENCIAL = "presencial"
    CLASS_TYPE_VIRTUAL = "virtual"
    CLASS_TYPE_CHOICES = [
        (CLASS_TYPE_PRESENCIAL, "Presencial"),
        (CLASS_TYPE_VIRTUAL, "Virtual"),
    ]

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    class_type = models.CharField(max_length=20, choices=CLASS_TYPE_CHOICES)
    credits = models.PositiveSmallIntegerField()
    weekly_hours = models.PositiveSmallIntegerField()
    capacity = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class SubjectGroup(TimeStampedModel):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="groups")
    identifier = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["subject__code", "identifier"]
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "identifier"],
                name="unique_subject_group_per_subject",
            )
        ]

    def __str__(self):
        return f"{self.subject.code} - {self.identifier}"


class WorkingDay(TimeStampedModel):
    day_of_week = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["day_of_week"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(day_of_week__gte=1, day_of_week__lte=7),
                name="workingday_valid_range",
            )
        ]

    def __str__(self):
        return f"{self.day_of_week} - {self.name}"


class TimeSlot(TimeStampedModel):
    name = models.CharField(max_length=80)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["start_time"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_time__gt=models.F("start_time")),
                name="timeslot_end_after_start",
            ),
            models.UniqueConstraint(
                fields=["name", "start_time", "end_time"],
                name="unique_timeslot_name_and_range",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.start_time}-{self.end_time})"


class SpaceType(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SubjectOffering(TimeStampedModel):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="offerings")
    subject_group = models.ForeignKey(
        SubjectGroup,
        on_delete=models.PROTECT,
        related_name="subject_offerings",
        null=True,
        blank=True,
    )
    academic_program = models.ForeignKey(
        AcademicProgram, on_delete=models.PROTECT, related_name="subject_offerings"
    )
    academic_period = models.ForeignKey(
        AcademicPeriod, on_delete=models.PROTECT, related_name="subject_offerings"
    )
    semester = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["academic_period", "semester", "subject__code", "subject_group__identifier"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(semester__gte=1),
                name="subject_offering_valid_semester",
            ),
            models.UniqueConstraint(
                fields=["academic_period", "subject_group", "academic_program", "semester"],
                name="unique_subject_offering_per_period_program_group_semester",
            ),
        ]

    def __str__(self):
        group_label = self.subject_group.identifier if self.subject_group else "Sin grupo"
        return f"{self.subject.code} | {group_label} | {self.academic_program.code} | S{self.semester}"
