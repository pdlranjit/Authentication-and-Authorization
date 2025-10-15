from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_no=models.CharField(max_length=12,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    college_name=models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.username
