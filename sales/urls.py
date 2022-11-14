from django.contrib import admin
from django.urls import path

from sales.views import SalesView

urlpatterns = [
    path('',SalesView.as_view(),name="all-sales")
]
