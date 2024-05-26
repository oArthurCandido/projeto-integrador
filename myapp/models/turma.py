from django.db import models

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    ano = models.TextField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ano', 'nome']

    def __str__(self):
        return f"{self.ano} - {self.nome}"