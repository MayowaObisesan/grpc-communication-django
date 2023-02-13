from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("currency", views.CurrencyViewSets, basename="currency")

urlpatterns = [
    path("", include(router.urls)),
    # path("users", views.UserViewSets.as_view(), name="users"),
]
