
from rest_framework import serializers
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