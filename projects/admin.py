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
            "fields": ("title", "slug", "short_description", "tech_stack", "description")
        }),
        ("Media (Static Images)", {
            "fields": ("image",),
            "description": "Use path like: images/projects/giftcard-app/giftcard-app.jpg"
        }),
        ("Links", {
            "fields": ("github_url", "live_url")
        }),
        ("Visibility", {
            "fields": ("featured",)
        }),
    )
