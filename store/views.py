from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Product
from .forms import  ProductForm
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/main_dashboard.html',context)


def add_new_product(request):
    context = {
        'form' : ProductForm()
    }
    if request.method == "POST":
        newProduct = ProductForm(request.POST)
        if newProduct.is_valid():
            new_product = newProduct.save()
            return render(request, 'store/products/page_new_product.html', context)
        else :
            return render(request, 'store/products/page_new_product.html',context)
    else:
        return render(request, 'store/products/page_new_product.html', context)
        
