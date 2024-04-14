from django.db import models
from .hora_aula import Hora_aula
from .disciplina import Disciplina
from .turma import Turma

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    hora_aula = models.ForeignKey(Hora_aula, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    