from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from common.models import Tariff


# Create your models here.
class PUser(AbstractUser):
    tel = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тариф')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')
    wallet = models.FloatField(default=0.0, verbose_name='Баланс')
    paid_date = models.DateTimeField(null=True, blank=True, verbose_name='Когда оплачено')
    number_of_files = models.IntegerField(default=1, verbose_name='Кол-во профилей (.conf)')
    file_path = models.CharField(max_length=255, null=True, blank=True, verbose_name='Путь к файлу')
