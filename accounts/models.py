from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
