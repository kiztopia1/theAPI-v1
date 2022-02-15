from django import forms
from .models import Item, Product


        
class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        
        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
