from datetime import datetime, timezone


def build_health_payload():
    return {
        "status": "ok",
        "service": "django-backend",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
