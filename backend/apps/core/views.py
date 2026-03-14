from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.health_service import build_health_payload


@api_view(["GET"])
def health_check(_request):
    return Response(build_health_payload())
