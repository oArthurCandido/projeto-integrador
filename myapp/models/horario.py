from django.db import models

class Horario(models.Model):
    inicio = models.TimeField()
    fim = models.TimeField()

    @property
    def str(self):
        return f"{self.inicio} - {self.fim}"

