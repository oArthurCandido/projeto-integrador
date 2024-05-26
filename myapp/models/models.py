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
    
class Hora_aula(models.Model):
    id = models.AutoField(primary_key=True)
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.horario_inicial} - {self.horario_final}"

class Horario(models.Model):
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return f"{self.inicio} - {self.fim}"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    horario = models.ForeignKey(Hora_aula, on_delete=models.CASCADE)
    segunda = models.ForeignKey(Disciplina, related_name='segunda', on_delete=models.SET_NULL, null=True, blank=True)
    terca = models.ForeignKey(Disciplina, related_name='terca', on_delete=models.SET_NULL, null=True, blank=True)
    quarta = models.ForeignKey(Disciplina, related_name='quarta', on_delete=models.SET_NULL, null=True, blank=True)
    quinta = models.ForeignKey(Disciplina, related_name='quinta', on_delete=models.SET_NULL, null=True, blank=True)
    sexta = models.ForeignKey(Disciplina, related_name='sexta', on_delete=models.SET_NULL, null=True, blank=True)

class Avisos(models.Model):
    identificacao = models.CharField(max_length=100)
    ano = models.CharField(max_length=10)
    aviso = models.TextField()

    def __str__(self):
        return f"{self.identificacao} - {self.ano}"