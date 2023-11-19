from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import VeiculoForm
from app.models import Veiculo

# Create your views here.

def home(request):
    return render(request,'principal/index.html')

def cadveiculos(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Veículo cadastrado com sucesso!')
                return redirect('cadveiculos')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar veículo: {e}')
    else:
        form = VeiculoForm()
    return render(request,'veiculos/cadveiculos.html',{'form':form})

def cadmotoristas(request):
    return render(request,'motoristas/cadmotoristas.html')

def movimentacao(request):
    return render(request,'movimentacao/movimentacao.html')
