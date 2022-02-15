from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import  ProductForm
# Create your views here.
def index(request):

    return render(request, 'store/main_dashboard.html',)


def add_new_product(request):
    if request.method == "POST":
        exit
    else:
        context = {
            'form' : ProductForm()
        }
        return render(request, 'store/products/page_new_product.html', context)
        
