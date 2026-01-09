from django.db import models


class HeroSection(models.Model):
    """
    Represents the main hero section on the homepage.
    This should usually have only ONE record.
    """

    name = models.CharField(
        max_length=100,
        help_text="Your name shown in hero section"
    )

    title = models.CharField(
        max_length=200,
        help_text="Main heading (e.g. Backend Developer)"
    )

    subtitle = models.TextField(
        help_text="Short description below the title"
    )

    primary_cta_text = models.CharField(
        max_length=50,
        default="View Projects"
    )

    secondary_cta_text = models.CharField(
        max_length=50,
        default="Contact Me"
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return f"Hero Section - {self.name}"
