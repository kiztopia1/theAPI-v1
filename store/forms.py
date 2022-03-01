from dataclasses import fields
from pyexpat import model
from unicodedata import category
from django import forms
from .models import Sale, Product


        
class ProductForm (forms.ModelForm):
    id = forms.CharField(required=False)
    category = forms.MultipleChoiceField(required=False)
    main_supplier = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    comments = forms.CharField(required=False)
    class Meta:
        model = Product
        fields = ('__all__')
        
        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                
                visible.field.widget.attrs['class'] = 'form-control'
    
class SaleForm (forms.ModelForm):
    products = forms.CharField(widget=forms.TextInput(attrs={'v-model':'products'}))
    total = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'v-model':'total'}))
    id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'v-model':'id'}))
    class Meta:
        model = Sale
        fields = ('products', 'total', 'id')