# urls.py
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', item_list_view, name='item-list'),
    path('add-supplier', add_supplier, name='add-supplier'),
    path('add-product', add_product, name='add-product'),
    path('list', product_list, name='product-list'),
    path('supplier-list', supplier_list, name='supplier-list'),
    path('add-productVariant', add_productVariant, name='add-productVariant'),
    path('productVariant-list', productVariant_list, name='productVariant-list'),
    path('product-variant-detail', product_variant_detail, name='product-variant-detail'),
    path('add-article', add_article, name='add-article')


    # other URL patterns...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
