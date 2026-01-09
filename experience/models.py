from django.db import models

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} @ {self.company}"
