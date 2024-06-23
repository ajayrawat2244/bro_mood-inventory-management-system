# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('list', outlet_list, name='outlet-list'),
    path('add-outlet', add_outlet, name='add-outlet')

    # other URL patterns...
]
