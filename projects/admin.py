from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured")
    list_filter = ("featured",)
    search_fields = ("title", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-id",)

    fieldsets = (
        ("Core Info", {
            "fields": ("title", "slug", "short_description", "description")
        }),
        ("Media", {
            "fields": ("image",)
        }),
        ("Links", {
            "fields": ("github_url", "live_url")
        }),
        ("Visibility", {
            "fields": ("featured",)
        }),
    )
