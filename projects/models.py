from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.CharField(
        max_length=255,
        help_text="Path inside static folder, e.g. images/projects/demo.jpg"
    )

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.slug])

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",")]


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="gallery",
        on_delete=models.CASCADE
    )
    image = models.CharField(
        max_length=255,
        help_text="Static path, e.g. images/projects/gallery/demo-1.jpg"
    )
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.project.title} image"

