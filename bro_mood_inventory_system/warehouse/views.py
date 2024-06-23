# views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def item_list_view(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def add_warehouse(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        state = request.POST.get("state")
        district = request.POST.get("district")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        contact_information = request.POST.get("contact_information")
        warehouse = Warehouse(name=name, state=state, district=district, city=city, pincode=pincode, contact_information=contact_information)
        warehouse.save()
        return redirect('/warehouse/list')
    return render(request,'warehouse/add_warehouse.html')

@login_required(login_url='login')
def warehouse_list(request):
    records_per_page = 10

    warehouse_list = Warehouse.objects.all()

    paginator = Paginator(warehouse_list, records_per_page)

    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'warehouse_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }
    return render(request, 'warehouse/warehouse_list.html', data)

# Create your views here.
