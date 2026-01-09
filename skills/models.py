from django.db import models


class Skill(models.Model):
    """
    Represents a technical skill.
    """

    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("database", "Database"),
        ("tools", "Tools"),
        ("devops", "DevOps"),
    ]

    name = models.CharField(
        max_length=100,
        help_text="Skill name (e.g. Django, PostgreSQL)"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        help_text="Skill category"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon class or emoji (e.g. 🐍)"
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Ordering of skills"
    )

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
