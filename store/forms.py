from unicodedata import category
from django import forms
from .models import Item, Product


        
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
    
