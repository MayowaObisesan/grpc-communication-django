from rest_framework import serializers
from core.models import Currency

class ListCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency()
        fields = [
            "id", "name", "code"
        ]
