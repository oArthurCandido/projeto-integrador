from django.db import models

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    ano = models.TextField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
class Hora_aula(models.Model):
    id = models.AutoField(primary_key=True)
    dia_semana = models.TextField(max_length=50)
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

