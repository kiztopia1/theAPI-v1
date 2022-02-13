from django import forms
from .models import Patient, History

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'age', 'sex', 'adress', 'phone1','language')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('description','medications','disease')
            
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'lab_result': forms.TextInput(attrs={'class': 'form-control'})
        }