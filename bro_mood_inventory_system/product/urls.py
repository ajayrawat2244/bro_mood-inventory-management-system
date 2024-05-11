# urls.py
from django.urls import path
from .views import item_list_view, product_list

urlpatterns = [
    path('', item_list_view, name='item-list'),
    path('list', product_list, name='item-list'),
    # other URL patterns...
]
