from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from tenant.manager import CustomUserManager

class SiteUser(AbstractUser):
    ''' Custom Site user Which is inherited from abstract base class .'''
    username = None
    email = models.CharField(max_length=30,unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    roles = models.CharField(max_length=30,default="user")
    objects = CustomUserManager()
