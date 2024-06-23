# views.py
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def item_list_view(request):
    return render(request, 'product/product_add.html')

@login_required(login_url='login')
def add_supplier(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_person = request.POST.get("contact_person")
        contact_information = request.POST.get("contact_information")
        address = request.POST.get("address")
        payment_terms = request.POST.get("payment_terms")
        mobile = request.POST.get("mobile")
        # brand = request.POST.get("brand")
        supplier = Supplier.objects.create(name=name, contact_person=contact_person,
                                           contact_information=contact_information, address=address,
                                           payment_terms=payment_terms, mobile=mobile)
        supplier.save()
        return redirect('/product/supplier-list')
    return render(request, 'supplier/supplier_add.html')

@login_required(login_url='login')
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        base_price = request.POST.get("base_price")
        brand = request.POST.get("brand")
        # reorder_level = request.POST.get("reorder_level")
        # supplier_id = int(request.POST.get("supplier"))
        # supplier = Supplier.objects.get(id=supplier_id)
        # print(Supplier)
        product = Product(name=name, description=description, category=category, brand=brand)
        product.save()
        return redirect('/product/list')
    return render(request, 'product/product_add.html')

@login_required(login_url='login')
def product_list(request):
    records_per_page = 10
    product_list = Product.objects.all()
    paginator = Paginator(product_list, records_per_page)
    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'product_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }
    return render(request, 'product/product_lst.html', data)

@login_required(login_url='login')
def supplier_list(request):
    records_per_page = 10
    supplier_list = Supplier.objects.all()
    paginator = Paginator(supplier_list, records_per_page)
    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'supplier_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }
    return render(request, 'supplier/supplier_list.html', data)

@login_required(login_url='login')
def add_productVariant(request):
    option2 = Product.objects.all()
    supplier_lst = Supplier.objects.all()
    if request.method == 'POST':
        product_id = int(request.POST.get("product"))
        product = Product.objects.get(id=product_id)
        image = request.FILES.get('image')
        supplier_id = int(request.POST.get("supplier"))
        supplier = Supplier.objects.get(id=supplier_id)
        # name = request.POST.get("name")
        color = request.POST.get("color")
        size_variant = request.POST.get("size_variant")
        supplier_price = request.POST.get("supplier_price")
        selling_price = request.POST.get("selling_price")
        customer_price = request.POST.get("customer_price")
        productVariant = ProductVariant(
            product=product, image=image, color=color, size_variant=size_variant,
            supplier_price=supplier_price, selling_price=selling_price, customer_price=customer_price,
            supplier = supplier
        )
        productVariant.save()
        productVariant.image.name = f"{productVariant.image.name}_{productVariant.id}"
        return redirect('/product/productVariant-list')
    print(supplier_lst[0])
    return render(request, 'product/productVariant_add.html', {'option2': option2, "supplier_lst": supplier_lst})

@login_required(login_url='login')
def productVariant_list(request):
    records_per_page = 10

    product_variant_list = ProductVariant.objects.all()

    paginator = Paginator(product_variant_list, records_per_page)

    page_number = request.GET.get('page')
    print(page_number, 2222)
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'product_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }

    return render(request, 'product/productVariant_list.html', data)

@login_required(login_url='login')
def product_variant_detail(request):
    product_variant_id = request.GET.get("product_variant_id")
    product_variant = ProductVariant.objects.get(id=product_variant_id)
    colors = [color.strip() for color in product_variant.color.split(",")]
    sizes = [size.strip() for size in product_variant.size_variant.split(",")]
    print(sizes, 55)
    return render(request, 'product/product_detail.html', {"product_variant": product_variant, "colors": colors, "sizes": sizes})
# Create your views here.
