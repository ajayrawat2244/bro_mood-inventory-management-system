from django.db import models
from django.contrib.auth.models import User

class Warehouse(models.Model):
     name = models.CharField(max_length=1000)
     state = models.CharField(max_length=50)
     district = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     pincode = models.CharField(max_length=6)
     contact_information = models.CharField(max_length=1000)
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     #todo need to e add warehose code