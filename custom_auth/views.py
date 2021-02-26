import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)

from .serializers import UserSerializer

class LoginAPIView(ObtainAuthToken):
    user_serializer = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            data = self.user_serializer(user)
            return Response(data.data, status=HTTP_200_OK)
        return Response({'error': 'Неверный логин или пароль'}, status=HTTP_400_BAD_REQUEST)



class LogoutAPIView(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response({}, status=HTTP_200_OK)
