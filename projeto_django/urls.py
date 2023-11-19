from django.urls import path

from app import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.home,name='index'),
    path('cadveiculos/',views.cadveiculos,name='cadveiculos'),
    path('cadmotoristas/',views.cadmotoristas,name='cadmotoristas'),
    path('movimentacao/',views.movimentacao,name='movimentacao'),
]
