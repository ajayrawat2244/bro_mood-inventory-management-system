# views.py
from django.shortcuts import render, redirect
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
        return redirect('/product/supplier-list')
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
        return redirect('/product/list')
    return render(request, 'product/product_add.html',{'options': options})

def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/product_lst.html', {'product_list':product_list})

def supplier_list(request):
    supplier_list = Supplier.objects.all()
    return render(request, 'product/supplier_list.html', {'supplier_list':supplier_list})
def add_productVariant(request):
    option2 = Product.objects.all()
    if request.method == 'POST':
        product_id = int(request.POST.get("product"))
        product = Product.objects.get(id=product_id)
        print(Product)
        name = request.POST.get("name")
        value = request.POST.get("value")
        productVariant = ProductVariant(product=product, name=name, value=value)
        productVariant.save()
        return redirect('/product/productVariant-list')
    return render(request, 'product/productVariant_add.html', { 'option2':option2 })
def productVariant_list(request):
    productVariant_list = ProductVariant.objects.all()
    return render(request, 'product/productVariant_list.html', {'productVariant_list':productVariant_list})
# Create your views here.

