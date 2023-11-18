from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'principal/index.html')

def cadveiculos(request):
    return render(request,'veiculos/cadveiculos.html')

def cadmotoristas(request):
    return render(request,'motoristas/cadmotoristas.html')

def movimentacao(request):
    return render(request,'movimentacao/movimentacao.html')
