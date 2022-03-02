
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
import json

from django.views import View

from .utils import update_stock
from .models import Product, Sale
from .forms import  ProductForm, SaleForm


from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A0
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


def to_object(text) :
    return json.loads(text)

# ____________________________________________________
def pdf(lines):
	buff = io.BytesIO()
	c = canvas.Canvas(buff, pagesize=A0, bottomup=0)
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica', 12)
	 

	

	for line in lines:
		textob.textLine(line)

	c.drawText(textob)
	c.showPage()
	c.save()
	buff.seek(0)
    # 
	return buff
def index(request):
    full_products = Product.objects.all()
    paged_products = Paginator(full_products, 10)
    product_no = request.GET.get('products')
    products = paged_products.get_page(product_no)

    full_sales = Sale.objects.all()
    paged_sales = Paginator(full_sales, 10)
    sale_no = request.GET.get('sale')
    sales = paged_sales.get_page(sale_no)
    
   
    # updates_sales = []
    # for a in sales :
    #     print(a,sales, '*********************')
    #     a['products'] = to_object(sale['procuts'])
    #     print(a['products'])

    context = {
        'products': products,
        'sales': sales,
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

def pos(request):
    context = {
        'form': SaleForm()
    }

    if request.method == 'POST':
        sale = Sale(
            id = request.POST['id'] ,
            products= request.POST['products'],
            total=request.POST['total'],
            seller= request.user.username
        )
        sale.save()
        lines = []
        products = to_object(request.POST['products'])
        # updateing all the stock values
        for product in products:
            update_stock(Product, product['amount'], product['id'])
            print(product['id'])

        for product in products:
            lines.append("------------------------------------------------")
            # lines.append(f'{}       {} X {}'.format(product['description'], product['amount']), product['price'])
            lines.append('{}      {} X {}'.format(product['description'],product['amount'], product['price']))
        res = pdf(lines)
        return FileResponse(res,as_attachment=True, filename='kira.pdf' ) 

    return render(request, 'store/pos/pos.html', context)
        
