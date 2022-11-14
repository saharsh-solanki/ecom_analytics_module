from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from tenant.views import SiteUser

class SiteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteUser
        fields = "__all__"
        extra_kwargs = {"is_staff": {"read_only": True}}

    def create(self, validated_data):
        user = SiteUser(**validated_data)
        user.password = make_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "email" in validated_data:
            del validated_data["email"]
        raise_errors_on_nested_writes('update', self, validated_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if "password" in validated_data:
            instance.password = make_password(validated_data["password"])
        instance.save()

        return instance

class MyTokenObtainPairSerializer(TokenObtainSerializer):
    default_error_messages = {
        'no_active_account': 'Please recheck Email address and Password.',
        'email_not_found': "We can not find any account associated with this email address.",
    }

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

