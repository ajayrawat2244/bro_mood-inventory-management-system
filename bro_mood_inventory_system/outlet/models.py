# from django.db import models
#
# class Outlet(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.TextField()
#     contact_information = models.CharField(max_length=100)
#
# class OutletInventory(models.Model):
#     outlet = models.ForeignKey('Outlet', on_delete=models.CASCADE)
#     product_variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
#     quantity_on_hand = models.PositiveIntegerField()
#
#
# class StockMovement(models.Model):
#     product_variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
#     outlet = models.ForeignKey('Outlet', on_delete=models.CASCADE)
#     movement_type = models.CharField(max_length=3, choices=[('IN', 'In'), ('OUT', 'Out')])
#     quantity = models.IntegerField()
#     date = models.DateField()
#     reference = models.CharField(max_length=100)
#
#
# class OutletTotalStock(models.Model):
#     outlet = models.ForeignKey('Outlet', on_delete=models.CASCADE)
#     product_variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
#     total_quantity = models.PositiveIntegerField()