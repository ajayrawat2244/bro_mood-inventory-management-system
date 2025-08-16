from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, blank=True)
    domain = models.URLField(blank=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Company_address(models.Model):
    state = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    pincode = models.CharField(max_length=6)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name

class UserProfile(models.Model):
    USER_ROLE = {
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
    parentuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="parentuser")
    mobile = models.BigIntegerField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, default=parentuser)
    userrole = models.CharField(choices=USER_ROLE, max_length=20, default='employee')
    #userstatus = models.IntegerField(choices=STATUS_CHOICE, default=1)
    #business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    #country_detail = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    #myplan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE, null=True, blank=True, related_name='myplan')

    def __str__(self):
        return str(self.user.username)



"""class Subuser(models.Model):
    CATEGORY_CHOICES = [
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    ]
    name = models.CharField(max_length=100)
    userid = models.TextField(null=True)
    password = models.CharField(max_length=128, null=True)
    role = models.CharField(choices=CATEGORY_CHOICES, default='employee', max_length=50)
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name"""

