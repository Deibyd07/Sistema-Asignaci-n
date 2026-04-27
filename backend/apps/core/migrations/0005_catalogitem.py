from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_workingday"),
    ]

    operations = [
        migrations.CreateModel(
            name="CatalogItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "catalog_type",
                    models.CharField(
                        choices=[
                            ("teacher_link_type", "Tipo de vinculacion docente"),
                            ("class_type", "Tipo de clase"),
                            ("academic_space_type", "Tipo de espacio academico"),
                        ],
                        max_length=40,
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["catalog_type", "name"],
            },
        ),
        migrations.AddConstraint(
            model_name="catalogitem",
            constraint=models.UniqueConstraint(
                fields=("catalog_type", "name"),
                name="unique_catalog_item_per_type",
            ),
        ),
    ]
