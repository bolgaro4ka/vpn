from django.contrib import admin
from .models import Tariff, Payment
# Register your models here.


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'ppm', 'description')
    search_fields = ('name', 'ppm', 'description')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user', 'created_at')
    list_filter = ('user', 'created_at')
    ordering = ('-created_at', 'user')
