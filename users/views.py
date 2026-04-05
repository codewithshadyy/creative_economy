from django.shortcuts import render

from .serializers import RegisterSerializer, PasswordResetRequestSerializer, NewPasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutRequestView(APIView): 
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist() 

            return Response({"message":"logged out"}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception:
            return Response({"error":"invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        
