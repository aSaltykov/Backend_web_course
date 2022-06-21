from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
import django.contrib.auth.password_validation as validators
from django.core.validators import validate_email
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'email': {'required': True},
                        'password': {'required': True}
                        }

    def validate_email(self, value):
        validate_email(value)
        profiles = User.objects.filter(username=value)
        if profiles.exists():
            raise exceptions.ValidationError({"user_email": ['Already exist']})
        else:
            return value

    def validate_password(self, value):
        validators.validate_password(password=value)
        return value

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        token = Token.objects.create(user=instance)
        ret['token'] = str(token)

        return ret

    def create(self, validated_data):
        username = validated_data['email']
        password = validated_data['password']

        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        return user
