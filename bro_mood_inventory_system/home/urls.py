# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', item_list_view, name='item-list'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('add-company', add_company, name='add-company')
    # other URL patterns...
]
