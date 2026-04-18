from django.db import migrations


DEFAULT_ROLES = [
    "Administrador",
    "Coordinador",
    "Docente",
    "Estudiante",
]


def seed_default_roles(apps, schema_editor):
    Role = apps.get_model("core", "Role")
    for role_name in DEFAULT_ROLES:
        Role.objects.get_or_create(
            name=role_name,
            defaults={"description": f"Rol funcional {role_name}"},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_userprofile_user"),
    ]

    operations = [
        migrations.RunPython(seed_default_roles, migrations.RunPython.noop),
    ]
