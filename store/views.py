from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ItemForm
# Create your views here.
def index(request):
    form = ItemForm();
    if request.method == 'POST':
        print (request.POST)
        item = ItemForm(request.POST)
        if item.is_valid():
            new_item = item.save()
            if new_item:
                messages.info(request, 'new item added')
            else:
                messages.info(request, 'not added')
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'store/main_dashboard.html', context)

