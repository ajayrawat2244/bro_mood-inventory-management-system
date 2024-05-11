# views.py
from django.shortcuts import render


def item_list_view(request):
    return render(request, 'product/product_add.html')


def product_list(request):
    return render(request, 'product/product_lst.html')

# Create your views here.
