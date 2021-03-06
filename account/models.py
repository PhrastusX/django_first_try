from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.FloatField()
    silver = models.FloatField()

