from typing import Any, Dict
from rest_framework import serializers
from user.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True)
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'created_at','updated_at', 'is_staff', 'is_active']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

        def create(self, **validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class LoginSerialier(TokenObtainPairSerializer):
   def validate(self, attrs):
       data = super().validate(attrs)
       refresh = self.get_token(user=self.user)
       user = UserSerializer(self.user).data
       data['refresh'] = str(refresh)
       data['access'] = str(refresh.access_token)
       data['user'] = user

       update_last_login(None, self.user)
       return data
       


