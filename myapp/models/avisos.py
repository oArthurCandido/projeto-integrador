from django.db import models
from .turma import Turma

class Avisos(models.Model):
    id = models.AutoField(primary_key=True)
    identificacao = models.CharField(max_length=100)
    #ano = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aviso = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.identificacao} - {self.turma}"

