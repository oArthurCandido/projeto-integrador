from django.db import models
from .turma import Turma

class Username(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    sexo = models.TextField(max_length=50)
    cpf = models.TextField(max_length=20, unique=True)
    data_nasc = models.DateField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)