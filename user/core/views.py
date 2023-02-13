# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters

from core.serializers import ListUserSerializer


# Initialize connection to the grpc server
import grpc
from gen_default_currency_pb2 import (
    DefaultCurrencyRequest,
    DefaultCurrencyResponse,
)
from gen_default_currency_pb2_grpc import CurrencyStub
from core.models import User

# Create the channel
channel = grpc.insecure_channel("localhost:50051")


class UserViewSets(viewsets.ModelViewSet):
    """User view sets"""

    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["email", "first_name", "last_name", "phone"]
    ordering_fields = [
        "last_login",
        "email",
        "first_name",
        "last_name",
        "phone",
    ]

    def perform_create(self, serializer):
        """Perform Post Create action of User Model"""
        print("On User save data")
        serializer.save()
        print(serializer.data, end="\n\n")
        client = CurrencyStub(channel)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).get()
        request = DefaultCurrencyRequest(user_id=user.id)
        print(f"request: {request}")
        response = client.generateDefaultCurrency(request)
        print(f"USER RESPONSE: {response}")
