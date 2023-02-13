from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import User


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "last_login",
            "default_currency_created",
        ]
