from django.contrib import admin
from django.urls import path,include
from .views import PackageView,SubscriptionView


urlpatterns = [
    path('packages/',PackageView.as_view(),name="packages for subscriptions"),
    path('subscriptions/',SubscriptionView.as_view(),name="subscriptions"),
]