from django.contrib import admin
from .models import Tariff, Payment, Tutorial
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

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_published')
    search_fields = ('name', 'description')
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at', 'name')