from django.contrib import admin
from .models import Company_address, Company, UserProfile

admin.site.register(Company)
admin.site.register(Company_address)
admin.site.register(UserProfile)
