from django.shortcuts import render
from .models import Experience

def experience_timeline(request):
    experiences = Experience.objects.all()

    return render(
        request,
        "experience/experience.html",
        {
            "experiences": experiences
        }
    )
