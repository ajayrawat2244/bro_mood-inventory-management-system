# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('list', warehouse_list, name='warehouse-list'),
    path('add-warehouse', add_warehouse, name='add-warehouse')

    # other URL patterns...
]
