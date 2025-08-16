from django.db import models
from django.contrib.auth.models import User
from home.models import Company, UserProfile

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('shirt', 'Shirt'),
        ('jeans', 'Jeans'),
        ('t-Shirt', 'T-Shirt')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, default='footwear', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # brand = models.CharField(max_length=100, null=True, blank=True)
    # reorder_level = models.PositiveIntegerField(default=0)
    # company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    # supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    # base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.brand + "- " + self.name


"""class Article(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    #customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    def __str__(self):
        return (self.product.name + "- " + self.size + "- " +  self.color)
"""
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    address = models.TextField()
    payment_terms = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, help_text="Enter a valid mobile number", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


"""class ProductVariant(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # (e.g., Red, Large, Casual)
    color = models.CharField(max_length=50, null=True)
    size = models.IntegerField(default=1)
    size_variant = models.CharField(default="", max_length=100, null=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    #customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product.name
"""