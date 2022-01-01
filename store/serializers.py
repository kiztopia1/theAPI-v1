from django.db import models
from django.db.models import fields
from rest_framework import serializers

from store.models import Item, SoldItem

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ( 'key', 'name', 'price', 'amount' )

class SoldItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SoldItem
        fields = ('item', 'saleId', 'amount', 'date')