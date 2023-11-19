from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from app.forms import VeiculoForm
from app.models import Veiculo

from app.forms import MotoristaForm
from app.models import Motorista

from app.forms import ControleForm
from app.models import ControleVeiculos


# Create your views here.


# PAGINA INICIAL
def home(request):
    controle_veiculos = ControleVeiculos.objects.all()
    return render(request,'principal/index.html',{'controle_veiculos': controle_veiculos})


# CADASTRO DE VEICULOS
def cadveiculos(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Veículo cadastrado com sucesso!')
                return redirect('cadveiculos')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar: {e}')
    else:
        form = VeiculoForm()
    return render(request,'veiculos/cadveiculos.html',{'form':form})


# CADASTRO DE MOTORISTAS
def cadmotoristas(request):
    if request.method == "POST":
        form = MotoristaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Motorista cadastrado com sucesso!')
                return redirect('cadmotoristas')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar: {e}')
    else:
        form = MotoristaForm()
    return render(request,'motoristas/cadmotoristas.html',{'form':form})


# CADASTRO DE MOVIMENTAÇÃO
def movimentacao(request):
    if request.method == "POST":
        form = ControleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print()
                messages.success(request, 'Movimentação cadastrada com sucesso!')
                return redirect('movimentacao')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar: {e}')
    else:
        form = ControleForm()
    return render(request,'movimentacao/movimentacao.html',{'form':form})


# EDIÇÃO DE CONTROLE
def edit(request, id_controle):
    id_controle = ControleVeiculos.objects.get(id_controle=id_controle)
    return render(request, 'movimentacao/edit.html',{'id_controle': id_controle})


# UPDATE DE CONTROLE
def update(request, id_controle):
    id_controle = ControleVeiculos.objects.get(id_controle=id_controle)
    form = ControleForm(request.POST, instance= id_controle)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'id_controle': id_controle})


# CONFIRMAÇÃO DE DELETE
def confirm_delete(request, id_controle):
    id_controle = get_object_or_404(ControleVeiculos, id_controle=id_controle)
    return render(request, 'confirm_delete.html', {'id_controle': id_controle})


# DELETE DE CONTROLE
def destroy(request, id_controle):
    if request.method == 'POST':     
        id_controle = get_object_or_404(ControleVeiculos, id_controle=id_controle)
        id_controle.delete()
        messages.success(request, 'Movimentação excluída com sucesso!')
        return redirect('/')
    return redirect('confirm_delete', id_controle=id_controle)
