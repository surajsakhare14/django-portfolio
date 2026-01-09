from django.urls import path
from .views import experience_timeline

urlpatterns = [
    path("", experience_timeline, name="experience"),
]
