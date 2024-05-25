from django.db import models
from .turma import Turma
from django.contrib.auth.models import User

class User_Turma(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
