from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)

