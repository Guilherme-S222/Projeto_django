from django.urls import path

from app_controle_veiculos import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.home,name='index'),
    path('cadveiculos/',views.cadveiculos,name='cadveiculos'),
    path('cadmotoristas/',views.cadmotoristas,name='cadmotoristas')
    
]
