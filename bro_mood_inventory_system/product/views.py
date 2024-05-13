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
    options = Supplier.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        base_price = request.POST.get("base_price")
        #reorder_level = request.POST.get("reorder_level")
        supplier_id = int(request.POST.get("supplier"))
        supplier = Supplier.objects.get(id=supplier_id)
        print(Supplier)
        product = Product(name=name, description=description, category=category, base_price=base_price, supplier=supplier)
        product.save()

    return render(request, 'product/product_add.html',{'options': options})

def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/product_lst.html', {'product_list':product_list})

# Create your views here.
