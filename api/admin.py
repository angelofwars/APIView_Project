from django.contrib import admin
from .models import DRF_Test

@admin.register(DRF_Test)
class DRF_TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')