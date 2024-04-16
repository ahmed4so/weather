from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class customers(models.Model):
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    Fullname = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Allow null if there are existing records without users
    Location = models.CharField(max_length=120)
    Phone = models.CharField(max_length=120)
    Password = models.CharField(max_length=120)
    gender = models.CharField(max_length=20, choices=Gender)







