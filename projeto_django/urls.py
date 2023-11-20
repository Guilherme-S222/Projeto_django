from django.urls import path

### Explicação do código ###
# O arquivo urls.py é responsável por definir as rotas(urls) do seu projeto e mapear essas urls para as funções ou classes de views correspondentes. Cada URLS é associada a uma view especifica.

from app import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.home,name='index'),
    path('cadveiculos/',views.cadveiculos,name='cadveiculos'),
    path('cadmotoristas/',views.cadmotoristas,name='cadmotoristas'),
    path('movimentacao/',views.movimentacao,name='movimentacao'),
    path('edit/<int:id_controle>', views.edit, name='edit'),
    path('update/<int:id_controle>', views.update, name='update'),
    path('confirm_delete/<int:id_controle>', views.confirm_delete, name='confirm_delete'),
    path('delete/<int:id_controle>', views.destroy, name='destroy'),
]
