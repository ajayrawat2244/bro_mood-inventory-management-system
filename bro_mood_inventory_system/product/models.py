from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    address = models.TextField()
    payment_terms = models.CharField(max_length=100)

class ProductVariant(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=50) # (e.g., Color, Size, Style)
    value = models.CharField(max_length=50) # (e.g., Red, Large, Casual)
