from django.db import models

class Warehouse(models.Model):
     name = models.CharField(max_length=1000)
     state = models.CharField(max_length=50)
     district = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     pincode = models.CharField(max_length=6)
     contact_information = models.CharField(max_length=1000)
     #todo need to e add warehose code