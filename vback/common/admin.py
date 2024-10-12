from django.contrib import admin
from .models import Tariff
# Register your models here.


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'ppm', 'description')
    search_fields = ('name', 'ppm', 'description')
