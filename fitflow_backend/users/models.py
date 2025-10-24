from django.db import models


# Create your models here.
class CustomUser(models.Model):
    display_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)