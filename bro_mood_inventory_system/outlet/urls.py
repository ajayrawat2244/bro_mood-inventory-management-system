# urls.py
from django.urls import path
from .views import item_list_view

urlpatterns = [
    path('items/', item_list_view, name='item-list'),
    # other URL patterns...
]
