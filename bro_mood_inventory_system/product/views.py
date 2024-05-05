# views.py
from django.shortcuts import render

def item_list_view(request):
    return render(request, 'product/product_add.html')


# Create your views here.
