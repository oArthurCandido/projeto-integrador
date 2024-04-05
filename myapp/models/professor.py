from django.db import models
from .endereco import Endereco
from .disciplina import Disciplina

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    cpf = models.TextField(max_length=20, unique=True)
    data_nasc = models.DateField()
    email = models.TextField(max_length=100)
    telefone = models.TextField(max_length=25)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    num_casa = models.TextField(max_length=10)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    