from django import forms
from app.models import Veiculo
from app.models import Motorista

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

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['cod_motorista', 'nome_motorista', 'telefone_motorista', 'cnh_motorista']
        widgets = {
            'cod_motorista': forms.NumberInput(attrs={ 'class': 'input' }),
            'nome_motorista': forms.TextInput(attrs={ 'class': 'input' }),
            'telefone_motorista': forms.TextInput(attrs={ 'class': 'input' }),
            'cnh_motorista': forms.TextInput(attrs={ 'class': 'input' }),
        }