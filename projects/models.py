from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    created_at = models.DateTimeField('Created at',auto_now_add=True)
    updated_at = models.DateTimeField('Updated at',auto_now=True)
    image = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title