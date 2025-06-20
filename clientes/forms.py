from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cicli': forms.TextInput(attrs={'class': 'input'}),
            'nombrecli': forms.TextInput(attrs={'class': 'input'}),
            'direccioncli': forms.TextInput(attrs={'class': 'input'}),
            'telefonocli': forms.TextInput(attrs={'class': 'input'}),
            'estadocli': forms.CheckboxInput(attrs={'class': 'ml-2'}),
        }
