from django.db import models

from tenant.models import SiteUser


class Sales(models.Model):
    ''' Models For Sales '''
    orderDate   = models.DateField(null=True,auto_now=True)
    region      = models.CharField(max_length=250,blank=False)
    manager     = models.ForeignKey(SiteUser,related_name="manager",on_delete=models.SET_NULL,null=True)
    salesPerson = models.ForeignKey(SiteUser,related_name="salesPerson",on_delete=models.SET_NULL,null=True)
    item        = models.CharField(max_length=250,blank=False)
    units       = models.IntegerField(default=1)
    unitPrice   = models.FloatField(null=False,blank=False)
    saleAmount  = models.FloatField(null=False,blank=False)