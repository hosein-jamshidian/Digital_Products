from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,GetTokenView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path("register/",RegisterView.as_view(),name="resigter"),
    #path("get-token/",GetTokenView.as_view(),name="get token"),
    # path("users/token/",TokenObtainPairView.as_view(),name="token obtain"),
    # path("users/token/refresh/",TokenRefreshView.as_view(),name="refresh token "),

    path("users/token/", TokenObtainPairView.as_view(), name="token obtain"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="refresh token "),

]
