# Create your views here.
from rest_framework import viewsets, filters

from core.serializers import ListCurrencySerializer
from core.models import Currency


class CurrencyViewSets(viewsets.ModelViewSet):
    """Currency view sets"""

    queryset = Currency.objects.all()
    serializer_class = ListCurrencySerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "code"]
    ordering_fields = ["name", "code"]
