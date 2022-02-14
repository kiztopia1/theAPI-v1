from django import forms
from .models import Item

class ItemForm (forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')
        
        widgets = {
            'key': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'alert': forms.CheckboxInput(attrs={'class': ''}),

        }
        
