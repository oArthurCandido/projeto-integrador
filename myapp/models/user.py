from django.db import models
from django.contrib.auth.models import User
from .turma import Turma

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turmas = models.ManyToManyField(Turma)
