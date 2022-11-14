from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from ecom_analytics_module import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/sales/', include('sales.urls')),
    path('api/tenant/', include('tenant.urls')),
]
