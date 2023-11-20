from django.db import models

# O models.py é responsável por definir a estrutura do banco de dados, especificando os modelos de dados que serão usados para armazenar e recuperar informações

# TABELA VEICULOS
class Veiculo(models.Model):  
    placa_veiculo = models.CharField(max_length=7, primary_key=True)  
    marca_veiculo = models.CharField(max_length=50)
    nome_veiculo = models.CharField(max_length=50)
    km_troca_oleo_veiculos = models.IntegerField()
   
    class Meta:  
        db_table = "veiculos"

# TABELA MOTORISTAS        
class Motorista(models.Model):  
    cod_motorista = models.IntegerField(primary_key=True)  
    nome_motorista = models.CharField(max_length=50)
    telefone_motorista = models.CharField(max_length=11)
    cnh_motorista = models.CharField(max_length=10)
   
    class Meta:  
        db_table = "motoristas"

# TABELA CONTROLE_VEICULOS                
class ControleVeiculos(models.Model):  
    id_controle = models.AutoField(primary_key=True)  
    placa_veiculo_FK = models.CharField(max_length=7)
    cod_motorista_FK = models.IntegerField()
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.IntegerField()
    destino = models.CharField(max_length=50)
    data_retorno = models.DateField()
    hora_retorno = models.TimeField()
    km_retorno = models.IntegerField()
    km_percorrido = models.IntegerField()
   
    class Meta:  
        db_table = "controle_veiculos"
