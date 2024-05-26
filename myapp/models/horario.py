from django.db import models

class Horario(models.Model):
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return f"{self.inicio} - {self.fim}"

