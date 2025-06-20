from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'cicli': 'CI',
            'nombrecli': 'Nombre',
            'direccioncli': 'Dirección',
            'telefonocli': 'Teléfono',
            'estadocli': 'Estado',
        }
        widgets = {
            'cicli': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'nombrecli': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'direccioncli': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'telefonocli': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'estadocli': forms.CheckboxInput(attrs={'class': 'h-5 w-5 text-blue-600'}),
        }
