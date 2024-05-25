from django.db import models

class Avisos(models.Model):
    identificacao = models.CharField(max_length=100)
    ano = models.CharField(max_length=10)
    aviso = models.TextField()

    def __str__(self):
        return f"{self.identificacao} - {self.ano}"