from django.db import models
from .hora_aula import Hora_aula
from .disciplina import Disciplina
from .turma import Turma

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    dia_semana = models.TextField(max_length=50)
    hora_aula = models.ForeignKey(Hora_aula, on_delete=models.SET_NULL, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.horario_inicial} - {self.horario_final}"
    
