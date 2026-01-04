from django.contrib import admin
from .models import DemoRequest

@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ("organization", "email", "created_at")
    search_fields = ("organization", "email")
