
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, max_length=8)


     class Meta:
          model = User
          fields = ['id', 'username', 'email', 'role', 'password']

     def create(self, validated_data):
          user = User.objects.create_user(
               
               username=validated_data["username"],
               email=validated_data["email"],
               password=validated_data["password"],
               role=validated_data["role"]

               
          )
        #   if user.objects.email:
        #        serializers.ValidationError("email exists")

          return user
     

class PasswordResetRequestSerializer(serializers.Serializer):
     email = serializers.EmailField()

     def validate(self, attrs):
          email = attrs["email"] 

          if User.objects.filter(email=email).exists():
               user = User.objects.get(email=email)
               uidb64 = urlsafe_base64_encode(force_bytes(user.id))
               token = PasswordResetTokenGenerator().make_token(user)
               reset_link = f"http://localhost:8000/api/auth/password-reset/{uidb64}/{token}/"

               send_mail(
                    "Password rset request",
                    f"kindly reset your password via this link:{reset_link}",
                    "creativeeconomy@gmail.com",
                    [user.email]
               )  
          return attrs


class NewPasswordSerializer(serializers.Serializer):
     password = serializers.CharField(max_length=10)
     uidb64 = serializers.CharField()
     token = serializers.CharField()

     def validate(self, attrs):
          try:
               user_id = smart_str(urlsafe_base64_decode(attrs["uidb64"]))
               user = User.objects.get(id=user)

               if not PasswordResetTokenGenerator().check_token(user,attrs["user"]):
                   raise serializers.ValidationError("oop! validation error")

               user.set_password(attrs["password"])
               user.save()
               return user
          except Exception:
             raise  serializers.ValidationError("invalisde reset link")  
          
             
