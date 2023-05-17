# from rest_framework import serializers
# from django.contrib.auth.password_validation import validate_password
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, validators=[validate_password])

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')


from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'phone', 'address')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
