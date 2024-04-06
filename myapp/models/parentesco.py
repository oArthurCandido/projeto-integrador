from django.db import models
from .aluno import Aluno
from .responsavel import Responsavel

class Parentesco(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    rel_aluno = models.TextField(max_length=100)
    rel_responsavel = models.TextField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    