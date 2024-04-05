from django.db import models

class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    dia_semana = models.models.TextField(max_length=50)
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)