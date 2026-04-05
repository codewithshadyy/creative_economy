from django.shortcuts import render

from .serializers import RegisterSerializer, PasswordResetRequestSerializer, NewPasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


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
        

class PasswordResetView(generics.GenericAPIView):

    
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]
              

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message" :"email sent successfully"})
    



class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = NewPasswordSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, uidb64, token):
        serializer = self.get_serializer(
            data={
                'password': request.data.get('password'),
                'uidb64': uidb64,
                'token': token
            }
        )
        serializer.is_valid(raise_exception=True)
        return Response({"detail": "Password reset successful."}  )  

            
