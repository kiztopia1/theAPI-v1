from pyexpat import model
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from store.models import Product, SoldItem, Item



# class SoldItemSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model= SoldItem
#         fields = ('item', 'saleId', 'amount', 'date',)

#     def to_representation(self, instance):
#         data =  super().to_representation(instance)
#         item = Item.objects.get(key=data['item'])
#         data['item'] = item.name
#         data['key'] = item.key
#         return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ('id', 'description', 'price')