from django.contrib import admin
from django.urls import path,include
from .views import GatewayView,PaymentView


urlpatterns = [
    path("gateways/",GatewayView.as_view(),name="all gateways"),
    path("pay/",PaymentView.as_view(),name="all payments"),
]


