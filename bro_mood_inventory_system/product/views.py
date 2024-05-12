# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *



def item_list_view(request):
    return render(request, 'product/product_add.html')
def add_supplier(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_person = request.POST.get("contact_person")
        contact_information = request.POST.get("contact_information")
        address = request.POST.get("address")
        payment_terms = request.POST.get("payment_terms")
        supplier = Supplier.objects.create(name=name, contact_person=contact_person, contact_information=contact_information, address=address, payment_terms=payment_terms)
        supplier.save()
        return HttpResponse("supplier added")
    return render(request, 'product/supplier_add.html')
def add_product(request):
    options = Supplier.objects.values_list('name', flat=True)
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        base_price = request.POST.get("base_price")
        reorder_level = request.POST.get("reorder_level")
        supplier = request.POST.get("supplier")
        product = Product.objects.create(name=name, description=description, category=category, base_price=base_price, reorder_level=reorder_level, supplier=supplier)
        product.save()
    return render(request, 'product/product_add.html',{'options': options})

def product_list(request):
    return render(request, 'product/product_list.html')

# Create your views here.
