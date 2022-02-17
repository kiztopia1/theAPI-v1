from django.contrib import admin
from .models import Supplier, Tax, Category, Product
# Register your models here.


admin.site.register(Tax)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)

