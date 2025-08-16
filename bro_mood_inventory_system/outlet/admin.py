from django.contrib import admin
from .models import Outlet, Journal#, AvailableStock, StockMovement

admin.site.register(Outlet)
#admin.site.register(AvailableStock)
#admin.site.register(StockMovement)
admin.site.register(Journal)
