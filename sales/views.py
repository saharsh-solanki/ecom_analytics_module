import operator
from datetime import date, timedelta
from functools import reduce

from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from sales.models import Sales
from sales.permissions import IsManager
from sales.serializers import SalesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SalesView(generics.ListAPIView,generics.CreateAPIView):
    ''' Sales View List the Sales With Different - Different Types of params , create sales  '''
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticated,IsManager]
    search_fields = ["item", ]
    ordering_fields = ['id', "saleAmount"]

    def get_queryset(self):
        query_list = []
        if "region" in self.request.query_params:
            if self.request.query_params.get("region"):
                query_list.append(Q(region=self.request.query_params.get("region")))
        if "date" in self.request.query_params:
            if self.request.query_params.get("date"):
                today = date.today()
                if self.request.query_params.get("date") == "last7d":
                    seven_day_before = today - timedelta(days=7)
                    query_list.append(Q(orderDate__gte=seven_day_before))
                if self.request.query_params.get("date") == "last1day":
                    pre_day = today - timedelta(days=1)
                    query_list.append(Q(orderDate__gte=pre_day))
                if self.request.query_params.get("date") == "last30day":
                    pre_day = today - timedelta(days=30)
                    query_list.append(Q(orderDate__gte=pre_day))
        if "manager" in self.request.query_params:
            if self.request.query_params.getlist("manager"):
                query_list.append(Q(manager__id=self.request.query_params.get("manager")))
        if "salesPerson" in self.request.query_params:
            if self.request.query_params.getlist("salesPerson"):
                query_list.append(Q(salesPerson__id=self.request.query_params.get("salesPerson")))
        if query_list:
            return super().get_queryset().filter(reduce(operator.and_, query_list)).distinct()
        else:
            return super().get_queryset()