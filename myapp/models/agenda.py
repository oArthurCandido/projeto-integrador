from django.db import models
from .disciplina import Disciplina
from .hora_aula import Hora_aula
from .turma import Turma

class Agenda(models.Model):
    horario = models.ForeignKey(Hora_aula, on_delete=models.SET_NULL, null=True, blank=True)
    segunda = models.ForeignKey(Disciplina, related_name='segunda', on_delete=models.SET_NULL, null=True, blank=True)
    terca = models.ForeignKey(Disciplina, related_name='terca', on_delete=models.SET_NULL, null=True, blank=True)
    quarta = models.ForeignKey(Disciplina, related_name='quarta', on_delete=models.SET_NULL, null=True, blank=True)
    quinta = models.ForeignKey(Disciplina, related_name='quinta', on_delete=models.SET_NULL, null=True, blank=True)
    sexta = models.ForeignKey(Disciplina, related_name='sexta', on_delete=models.SET_NULL, null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)