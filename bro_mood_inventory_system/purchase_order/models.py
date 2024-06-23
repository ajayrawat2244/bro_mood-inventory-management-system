from django.db import models
from warehouse.models import Warehouse
from product.models import Supplier, Product, ProductVariant
import datetime

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('issued', 'ISSUED'),
        ('inprogress', 'INPROGRESS'),
        ('completed', 'COMPLETED')
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'PENDING'),
        ('completed', 'COMPLETED')
    ]
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    order_date = models.DateField(null=True)
    shipping_cost = models.IntegerField(default=0)
    order_status = models.CharField(choices=STATUS_CHOICES, default='issued', max_length=10, null=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, default='pending', max_length=10, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expected_delivery_date = models.DateField(null=True)
    payment_due_date = models.DateField(null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    approved_date = models.DateField(null=True, blank=True)
    shipment_date = models.DateField(null=True, blank=True)
    shipping_method = models.TextField(default='xyz')
    payment_method = models.TextField(default='COD')

    def update_total_amount(self):
        total_items_cost = PurchaseOrderItem.objects.filter(purchase_order=self).aggregate(
            total=models.Sum('total_bill')
        )['total'] or 0.00
        self.total_amount = total_items_cost + self.shipping_cost + self.tax
        self.save(update_fields=['total_amount'])

class PurchaseOrderItem(models.Model):
     purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)
     product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

     description = models.TextField()
     purchase_demand = models.IntegerField(default=1)
     actual_purchase = models.IntegerField(default=1)
     unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
     total_bill = models.DecimalField(max_digits=10, decimal_places=2)
     order_date = models.DateField(null=True, default=datetime.date.today)
     sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

     def save(self, *args, **kwargs):
         super(PurchaseOrderItem, self).save(*args, **kwargs)
         self.update_sub_total()

     def update_sub_total(self):
         sub_total = PurchaseOrderItem.objects.filter(purchase_order=self.purchase_order).aggregate(
             total=models.Sum('total_bill')
         )['total'] or 0.00
         self.sub_total = sub_total
         super(PurchaseOrderItem, self).save(update_fields=['sub_total'])

     def __str__(self):
         return f'Item {self.id} for Purchase Order {self.purchase_order.id}'

     """def save(self, *args, **kwargs):
         self.total_bill = self.actual_purchase * self.unit_price
         super(PurchaseOrderItem, self).save(*args, **kwargs)
         self.update_sub_total()

     def update_sub_total(self):
         sub_total = PurchaseOrderItem.objects.filter(purchase_order=self.purchase_order).aggregate(
             total=models.Sum('total_bill')
         )['total'] or 0.00
         self.purchase_order.total_amount = sub_total
         self.purchase_order.save(update_fields=['total_amount'])

     def __str__(self):
         return f'Item {self.id} for Purchase Order {self.purchase_order.id}'"""



