from django.contrib import admin
from .models import PUser
# Register your models here

admin.site.site_header = "PVPN Админка"

@admin.register(PUser)
class PUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')


