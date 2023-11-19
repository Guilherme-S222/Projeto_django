from django import forms
from app.models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa_veiculo', 'marca_veiculo', 'nome_veiculo', 'km_troca_oleo_veiculos']
        widgets = {
            'placa_veiculo': forms.TextInput(attrs={ 'class': 'input' }),
            'marca_veiculo': forms.TextInput(attrs={ 'class': 'input' }),
            'nome_veiculo': forms.TextInput(attrs={ 'class': 'input' }),
            'km_troca_oleo_veiculos': forms.NumberInput(attrs={ 'class': 'input' }),
        }