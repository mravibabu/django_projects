from django.db import models

# Create your models
from datetime import date

class Blog (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()