# Generated by Django 4.2.7 on 2023-11-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControleVeiculos',
            fields=[
                ('id_controle', models.IntegerField(primary_key=True, serialize=False)),
                ('placa_veiculo_FK', models.CharField(max_length=7)),
                ('cod_motorista_FK', models.IntegerField()),
                ('data_saida', models.DateField()),
                ('hora_saida', models.TimeField()),
                ('km_saida', models.IntegerField()),
                ('destino', models.CharField(max_length=50)),
                ('data_retorno', models.DateField()),
                ('hora_retorno', models.TimeField()),
                ('km_retorno', models.IntegerField()),
                ('km_percorrido', models.IntegerField()),
            ],
            options={
                'db_table': 'controle_veiculos',
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('cod_motorista', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_motorista', models.CharField(max_length=50)),
                ('telefone_motorista', models.CharField(max_length=11)),
                ('cnh_motorista', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'motoristas',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('placa_veiculo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('marca_veiculo', models.CharField(max_length=50)),
                ('nome_veiculo', models.CharField(max_length=50)),
                ('km_troca_oleo_veiculos', models.IntegerField()),
            ],
            options={
                'db_table': 'veiculos',
            },
        ),
    ]
