# views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from product.models import Supplier, Product, ProductVariant
from warehouse.models import Warehouse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def item_list_view(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def add_purchase_order(request):
    item = ProductVariant.objects.all()
    warehouses = Warehouse.objects.all()
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        warehouse_id = int(request.POST.get('warehouse'))
        warehouse =Warehouse.objects.get(id=warehouse_id)
        supplier_id = int(request.POST.get('supplier'))
        supplier = Supplier.objects.get(id=supplier_id)
        order_date = request.POST.get('date')
        expected_delivery_date = request.POST.get('expectedDeliveryDate')
        purchase_order = PurchaseOrder(warehouse=warehouse, supplier=supplier, order_date=order_date,
                                       expected_delivery_date=expected_delivery_date)
        purchase_order.save()

        product_list = request.POST.getlist('product[]')
        actual_purchase_list = request.POST.getlist('actual_purchase[]')
        total_bill_list = request.POST.getlist('itemTotalPrice[]')
        description = request.POST.getlist('itemDescription[]')
        unit_price = request.POST.getlist('itemUnitPrice[]')
        for products,actual_purchase,total_bill, description, unit_price in zip(product_list, actual_purchase_list,
                                                                    total_bill_list, description, unit_price):
            product = ProductVariant.objects.get(id=int(products))
            PurchaseOrderItem.objects.create(
                purchase_order=purchase_order,
                description=description,
                order_date=order_date,
                product=product,
                unit_price=unit_price,
                actual_purchase=actual_purchase,
                total_bill=total_bill
            )
        return redirect('purchase-order-list')
    return render(request,'purchase_order/add_purchase_order.html',
                  {'item': item, 'warehouses':warehouses, 'suppliers':suppliers})

@login_required(login_url='login')
def get_purchase_order_details(request):
    purchase_order_id = request.GET.get('purchase_order_id')
    purchase_order = PurchaseOrder.objects.get(id=purchase_order_id)


    return render(request,'purchase_order/add_purchase_order.html')

@login_required(login_url='login')
def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    purchase_order_items = []

    for order in purchase_orders:
        last_item = PurchaseOrderItem.objects.filter(purchase_order=order).order_by('-id').first()
        if last_item:
            purchase_order_items.append({
                'order': order,
                'last_item_sub_total': last_item.sub_total
            })

    return render(request, 'purchase_order/purchase_order_list.html', {
        'purchase_order_items': purchase_order_items})

def purchase_order_detail(request):
    purchase_order_id = request.GET.get('purchase_order_id')
    purchase_order = PurchaseOrder.objects.get(id=purchase_order_id)
    order_item_list = PurchaseOrderItem.objects.filter(purchase_order=purchase_order)
    return render(request,'purchase_order/purchase_order_detail.html',
                  {'purchase_order':purchase_order, 'order_item_list':order_item_list})


# Create your views here.
