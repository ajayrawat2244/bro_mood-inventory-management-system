# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('list', outlet_list, name='outlet-list'),
    path('add-outlet', add_outlet, name='add-outlet'),
    path('add-stock', add_stock, name='add-stock'),
    path('availableStock-list', available_stock_list, name='stock-list'),
    path('add-journal', add_journal, name='add-journal'),
    path('journal-list', journal_list, name='journal-list')

    # other URL patterns...
]
