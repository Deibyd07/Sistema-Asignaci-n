from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_catalogitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=120, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("hourly_rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "link_type",
                    models.ForeignKey(
                        limit_choices_to={"catalog_type": "teacher_link_type"},
                        on_delete=models.deletion.PROTECT,
                        related_name="teachers",
                        to="core.catalogitem",
                    ),
                ),
            ],
            options={"ordering": ["last_name", "first_name"]},
        ),
        migrations.CreateModel(
            name="Classroom",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=120)),
                ("capacity", models.PositiveIntegerField()),
                ("is_accessible", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "campus",
                    models.ForeignKey(
                        on_delete=models.deletion.PROTECT,
                        related_name="classrooms",
                        to="core.campus",
                    ),
                ),
                (
                    "space_type",
                    models.ForeignKey(
                        limit_choices_to={"catalog_type": "academic_space_type"},
                        on_delete=models.deletion.PROTECT,
                        related_name="classrooms",
                        to="core.catalogitem",
                    ),
                ),
            ],
            options={"ordering": ["code"]},
        ),
        migrations.CreateModel(
            name="AcademicProgram",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=150)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "campus",
                    models.ForeignKey(
                        on_delete=models.deletion.PROTECT,
                        related_name="programs",
                        to="core.campus",
                    ),
                ),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=150)),
                ("credits", models.PositiveSmallIntegerField()),
                ("weekly_hours", models.PositiveSmallIntegerField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "academic_program",
                    models.ForeignKey(
                        on_delete=models.deletion.PROTECT,
                        related_name="courses",
                        to="core.academicprogram",
                    ),
                ),
                (
                    "class_type",
                    models.ForeignKey(
                        limit_choices_to={"catalog_type": "class_type"},
                        on_delete=models.deletion.PROTECT,
                        related_name="courses",
                        to="core.catalogitem",
                    ),
                ),
            ],
            options={"ordering": ["code"]},
        ),
        migrations.CreateModel(
            name="CourseGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("identifier", models.CharField(max_length=30)),
                ("student_count", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "course",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="groups", to="core.course"),
                ),
            ],
            options={"ordering": ["course_id", "identifier"]},
        ),
        migrations.AddConstraint(
            model_name="teacher",
            constraint=models.CheckConstraint(check=models.Q(("hourly_rate__gt", 0)), name="teacher_hourly_rate_positive"),
        ),
        migrations.AddConstraint(
            model_name="classroom",
            constraint=models.CheckConstraint(check=models.Q(("capacity__gt", 0)), name="classroom_capacity_positive"),
        ),
        migrations.AddConstraint(
            model_name="academicprogram",
            constraint=models.UniqueConstraint(fields=("campus", "name"), name="unique_program_name_per_campus"),
        ),
        migrations.AddConstraint(
            model_name="course",
            constraint=models.CheckConstraint(check=models.Q(("credits__gt", 0)), name="course_credits_positive"),
        ),
        migrations.AddConstraint(
            model_name="course",
            constraint=models.CheckConstraint(check=models.Q(("weekly_hours__gt", 0)), name="course_weekly_hours_positive"),
        ),
        migrations.AddConstraint(
            model_name="coursegroup",
            constraint=models.UniqueConstraint(fields=("course", "identifier"), name="unique_group_identifier_per_course"),
        ),
    ]
