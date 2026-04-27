from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_subjectgroup_and_subjectoffering_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="capacity",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="class_type",
            field=models.CharField(
                choices=[("presencial", "Presencial"), ("virtual", "Virtual")],
                default="presencial",
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="credits",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="difficulty",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="weekly_hours",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
