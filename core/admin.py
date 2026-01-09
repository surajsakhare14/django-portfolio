from django.contrib import admin
from .models import HeroSection


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    """
    Admin configuration for Hero Section
    """

    list_display = ("name", "title", "updated_at")
    readonly_fields = ("updated_at",)
