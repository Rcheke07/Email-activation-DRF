from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=6)
    class Meta:
        model=User
        fields=['email','username','password']

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(max_length=200)  
    username=serializers.CharField(max_length=60)

     