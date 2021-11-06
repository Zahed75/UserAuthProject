from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=55)
    email=models.EmailField(max_length=44)
    password=models.CharField(max_length=55)
