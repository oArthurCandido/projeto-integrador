from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.TextField(max_length=200)
    bairro = models.TextField(max_length=100)
    cidade = models.TextField(max_length=100)
    estado = models.TextField(max_length=100)
    cep = models.TextField(max_length=20, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)