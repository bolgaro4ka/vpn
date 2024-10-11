from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


# Create your models here.
class PUser(AbstractUser):
    tel = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)

