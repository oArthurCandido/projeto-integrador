from django.db import models

class Hora_aula(models.Model):
    id = models.AutoField(primary_key=True)
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)