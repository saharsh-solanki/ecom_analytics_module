from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from tenant.views import MyTokenObtainPairView, SiteUserView

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="ObtainedToken"),
    path("token/verify/", TokenVerifyView.as_view(), name="VerifyTokenValidity"),
    path("token/refresh/", TokenRefreshView.as_view(), name="RefreshToken"),
    path("user/", SiteUserView.as_view(), name="createUserView"),
]
