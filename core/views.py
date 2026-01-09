from django.shortcuts import render
from .models import HeroSection
from projects.models import Project


def home(request):
    hero = HeroSection.objects.first()  # only one record expected
    projects = Project.objects.filter(featured=True)

    return render(
        request,
        "home/index.html",
        {
            "hero": hero,
            "projects": projects
        }
    )
