from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,GetTokenView

urlpatterns = [
    path("register/",RegisterView.as_view(),name="resigter"),
    path("get-token/",GetTokenView.as_view(),name="get token"),
]
