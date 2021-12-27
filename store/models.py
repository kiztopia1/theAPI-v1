from django.db import models

# Create your models here.


class Item(models.Model):
    key = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    # sellingPrice = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    # expDate = models.DateField()


    def __str__(self):
        return self.name


class SoldItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    saleId = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.item.name