from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)

from mercedes.permissions import IsSuperUser
from core.tasks import update_db

class UpdateDBAPIView(APIView):
    permission_classes=[IsSuperUser]

    def get(self, request):
        update_db.delay(user_id=request.user.id)
        return Response({ 'message': 'update started' }, status=HTTP_200_OK)
