from django.db import models
from django.contrib.auth.models import User
from home.models import UserProfile, Company
from product.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class Outlet(models.Model):
     name = models.CharField(max_length=1000)
     #address = models.TextField()
     state = models.CharField(max_length=50)
     district = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     pincode = models.CharField(max_length=6)
     contact_information = models.CharField(max_length=1000)
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     #company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
     #todo need to be add outlet code
     #todo need to be add warehouse as a foreign key
     def __str__(self):
          return self.name

class Journal(models.Model):
    CATEGORY_CHOICES = [
        ('Shoe', 'Shoe'),
        ('Shirt', 'Shirt'),
        ('Jeans', 'Jeans'),
        ('T-Shirt', 'T-Shirt')
    ]
    serial_no = models.AutoField(primary_key=True)
    article = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2,)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, null=True, blank=True)
    register_date = models.DateField(null=False)
    credit_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
         return str(self.article)+ " "+str(self.register_date)+ " (credit-"+str(self.credit)+")"


"""class AvailableStock(models.Model):
     CATEGORY_CHOICES = [
          ('footwear', 'Footwear'),
          ('shirt', 'Shirt'),
          ('jeans', 'Jeans'),
          ('t-Shirt', 'T-Shirt')
     ]
     #outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
     #product = models.CharField(max_length=40, null=True)
     #category = models.CharField(choices=CATEGORY_CHOICES, default='footwear', max_length=50, null=True, blank=True)
     article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
     #todo remmove product and category, will imoact stock mmovement as well
     total_money_invested = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
     total_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
     remaining_quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     #company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
     def __str__(self):
           return (self.article.product.name + "- " + self.article.size + "- " +  self.article.color)

class StockMovement(models.Model):
     article= models.ForeignKey(AvailableStock, on_delete=models.SET_NULL, null=True)
     #product = models.ForeignKey(AvailableStock, on_delete=models.CASCADE, null=True)
     movement_type = models.CharField(max_length=3, choices=[('IN', 'In'), ('OUT', 'Out')], null=True)
     #quantity_detail =
     quantity = models.IntegerField(null=True, blank=True)
     unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
     #customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
     amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
     payment_medium = models.CharField(max_length=6, choices=[('ONLINE', 'Online'), ('CASH', 'Cash')], null=True, blank=True)
     date = models.DateField(null=True, blank=True)
     reference = models.CharField(max_length=1000, null=True, blank=True)
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     #company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

     def __str__(self):
          return (str(self.article)+ "." + self.movement_type + " " +  str(self.date))


@receiver(post_save, sender=StockMovement)
def update_money_invested(sender, instance, **kwargs):
     available_stock = instance.article
     if instance.movement_type == 'IN':

          # Calculate the money invested based on the quantity and unit price
          total_investment = instance.quantity * instance.unit_price
          incoming_stock = instance.quantity

          # Update the money_invested attribute
          available_stock.total_money_invested += total_investment
          available_stock.remaining_quantity += incoming_stock

          # Save the updated AvailableStock record
          available_stock.save()
     elif instance.movement_type == 'OUT':
          roi = instance.amount
          outgoing_stock = instance.quantity

          available_stock.total_roi += roi
          available_stock.remaining_quantity -= outgoing_stock
          available_stock.save()


"""

#class OutletInventory(models.Model):
#     outlet = models.ForeignKey('Outlet', on_delete=models.CASCADE)
#     product_variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
#     quantity_on_hand = models.PositiveIntegerField()


# class OutletTotalStock(models.Model):
#     outlet = models.ForeignKey('Outlet', on_delete=models.CASCADE)
#     product_variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
#     total_quantity = models.PositiveIntegerField()