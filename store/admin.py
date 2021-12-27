from django.contrib import admin
from .models import Item, SoldItem
# Register your models here.


admin.site.register(Item)
admin.site.register(SoldItem)