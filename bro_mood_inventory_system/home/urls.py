# urls.py
from django.urls import path
from .views import item_list_view, login, register

urlpatterns = [
    path('', item_list_view, name='item-list'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    # other URL patterns...
]
