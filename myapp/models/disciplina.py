from django.db import models

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    disciplina = models.TextField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)