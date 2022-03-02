from datetime import date
from statistics import mode
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField
from sqlalchemy import false, true



# Create your models here.


class Item(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    # sellingPrice = models.CharField(max_length=100)
    amount = models.IntegerField ()
    alert = models.BooleanField(default=False)
    minAmount = models.IntegerField(default=10)

    # expDate = models.DateField()


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return self.name
'''class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return super().__str__()'''
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tax(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.CharField(max_length=100, primary_key=True, )
    ENA_GTIN = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, default='', )
    sku = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    main_supplier = models.ManyToManyField(Supplier)
    #reference = models.CharField(max_length=100, null=True, blank=True)
    brand =  models.CharField(max_length=100, default='')
    comments = models.TextField(default='')

    #reserved_stock = models.IntegerField(default=0)
    #available_stock = models.IntegerField(default=0)
    min_stock = models.IntegerField(default=0)
    max_stock = models.IntegerField(default=0)
    #low_stock = models.IntegerField(default=0)
    stock_level = models.IntegerField(default=0)
    stock_alert = models.BooleanField(default=False)

    #reward = models.BooleanField(default=False)
    #point_needed = models.IntegerField()

    #taxation = models.CharField(max_length=100, blank=True)
    net_weight = models.CharField(max_length=100, blank=True, default='0')
    gross_weight = models.CharField(max_length=100, blank=True, default='0')
    #unit = models.CharField(max_length=100, choices=['Kg', 'Can', 'Meter', 'Piece'] )

    #added_in = models.CharField(max_length=100, blank=True)
    #modified_in = models.DateTimeField(max_length=100, blank=True)
    # user forign key
    #modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #commission = models.CharField(max_length=100, blank=True)
    #location = models.CharField(max_length=100, blank=True)

    #on_sale = models.BooleanField(default=False)
    #on_sale_init_day = models.DateTimeField( blank=True)
    #on_sale_final_day = models.DateTimeField(blank=True)
    #promotional = models.BooleanField()
    #status = models.BooleanField(default=False)
    tax = models.IntegerField(default=15)
    #bundle = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.description
class SoldItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    saleId = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.item

class Sale(models.Model):
    id = models.CharField(max_length=100, primary_key=True )
    date= models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    products = models.TextField()
    customer = models.CharField(default='unknown', max_length=100)
    total = models.IntegerField()
    # seller = models.CharField()

    # amount, change , shipment , discount, paid
    def __str__(self):
        return self.id