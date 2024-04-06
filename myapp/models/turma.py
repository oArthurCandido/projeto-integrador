from django.db import models

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    periodo = models.TextField(max_length=20)
    num_sala = models.TextField(max_length=5)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)