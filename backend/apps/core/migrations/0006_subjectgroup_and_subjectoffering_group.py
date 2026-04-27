from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_academicprogram_subject_subjectoffering"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubjectGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("identifier", models.CharField(max_length=80)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="groups",
                        to="core.subject",
                    ),
                ),
            ],
            options={
                "ordering": ["subject__code", "identifier"],
            },
        ),
        migrations.AddConstraint(
            model_name="subjectgroup",
            constraint=models.UniqueConstraint(
                fields=("subject", "identifier"),
                name="unique_subject_group_per_subject",
            ),
        ),
        migrations.AddField(
            model_name="subjectoffering",
            name="subject_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subject_offerings",
                to="core.subjectgroup",
            ),
        ),
        migrations.AlterModelOptions(
            name="subjectoffering",
            options={"ordering": ["academic_period", "semester", "subject__code", "subject_group__identifier"]},
        ),
        migrations.RemoveConstraint(
            model_name="subjectoffering",
            name="unique_subject_offering_per_period_program_semester",
        ),
        migrations.AddConstraint(
            model_name="subjectoffering",
            constraint=models.UniqueConstraint(
                fields=("academic_period", "subject_group", "academic_program", "semester"),
                name="unique_subject_offering_per_period_program_group_semester",
            ),
        ),
    ]
