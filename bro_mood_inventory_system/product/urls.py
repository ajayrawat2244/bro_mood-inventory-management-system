# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', item_list_view, name='item-list'),
    path('add-supplier', add_supplier, name='add-supplier'),
    path('add-product', add_product, name='add-product'),
    path('list', product_list, name='product-list'),
    path('supplier-list', supplier_list, name='supplier-list'),
    path('add-productVariant', add_productVariant, name='add-productVariant'),
    path('productVariant-list', productVariant_list, name='productVariant-list')

    # other URL patterns...
]
