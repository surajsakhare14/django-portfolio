from django.shortcuts import render
from .models import Skill


def skill_list(request):
    """
    Displays all skills grouped by category.
    """
    skills = Skill.objects.all()

    categories = {}
    for skill in skills:
        categories.setdefault(skill.category, []).append(skill)

    return render(
        request,
        "skills/skills.html",
        {
            "categories": categories,
            "skills": skills,
        }
    )
