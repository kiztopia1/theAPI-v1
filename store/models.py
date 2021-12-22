from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sellingPrice = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    expDate = models.DateField()


    def __str__(self):
        return self.name


class soldItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.item.name