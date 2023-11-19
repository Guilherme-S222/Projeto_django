from django import forms
from app.models import Veiculo
from app.models import Motorista
from app.models import ControleVeiculos


# VEICULOS
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


# MOTORISTAS
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

    
# CONTROLE DE VEICULOS E MOTORISTAS        
class ControleForm(forms.ModelForm):
    
    #placa_veiculo_FK = forms.ModelChoiceField(queryset=Veiculo.objects.all(), empty_label='Selecione uma opção')
    #cod_motorista_FK = forms.ModelChoiceField(queryset=Motorista.objects.all(), empty_label='Selecione uma opção')
    
    class Meta:
        model = ControleVeiculos
        fields = ['placa_veiculo_FK', 'cod_motorista_FK', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno', 'km_percorrido']
        widgets = {
            'placa_veiculo_FK': forms.TextInput(attrs={ 'class': 'input' }),
            'cod_motorista_FK': forms.NumberInput(attrs={ 'class': 'input' }),
            'data_saida': forms.DateInput(attrs={ 'class': 'input', 'type': 'date' }),
            'hora_saida': forms.TimeInput(attrs={ 'class': 'input', 'type': 'time' }),
            'km_saida': forms.NumberInput(attrs={ 'class': 'input' }),
            'destino': forms.TextInput(attrs={ 'class': 'input' }),
            'data_retorno': forms.DateInput(attrs={ 'class': 'input', 'type': 'date' }),
            'hora_retorno': forms.TimeInput(attrs={ 'class': 'input', 'type': 'time' }),
            'km_retorno': forms.NumberInput(attrs={ 'class': 'input' }),
            'km_percorrido': forms.NumberInput(attrs={ 'class': 'input' }),
        }