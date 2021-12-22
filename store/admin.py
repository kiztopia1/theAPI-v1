from django.contrib import admin
from .models import Item, soldItems
# Register your models here.


admin.site.register(Item)
admin.site.register(soldItems)