from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_seed_default_roles"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkingDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("day_of_week", models.PositiveSmallIntegerField(unique=True)),
                ("name", models.CharField(max_length=20, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["day_of_week"],
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(day_of_week__gte=1, day_of_week__lte=7),
                        name="workingday_valid_range",
                    )
                ],
            },
        ),
    ]
