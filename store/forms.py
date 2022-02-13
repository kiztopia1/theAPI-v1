from django import forms
from .models import Item

class ItemForm (forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')
        
        widgets = {
            'key': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'alert': forms.CheckboxInput(attrs={'class': ''}),

        }
        
