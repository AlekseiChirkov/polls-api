from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework import serializers

from apps.authentication.exceptions import DuplicateUsernameException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)
    password2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        fields = [
            'username', 'first_name', 'last_name', 'password', 'password2'
        ]

    def create(self, validated_data):
        try:
            user = User.objects.create(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
        except IntegrityError:
            raise DuplicateUsernameException

        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        user.set_password(validated_data['password'])
        user.save()
        return user



