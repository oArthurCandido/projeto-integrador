from django.db import models
from django.contrib.auth.models import Username

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    ano = models.TextField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

#class Username(models.Model):
#    user = models.OneToOneField(Username, on_delete=models.CASCADE)
#    turmas = models.ManyToManyField(Turma)
