from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)

from mercedes.permissions import IsSuperUser

class UpdateAPIView(APIView):
    permission_classes=[IsSuperUser]
    update_function = None

    def get(self, request):
        if self.update_function:
            self.update_function.delay(user_id=request.user.id)
            return Response({ 'message': 'update started' }, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
