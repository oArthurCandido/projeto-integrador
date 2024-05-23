from django.contrib import admin
from myapp.models.export_models import Aluno, Disciplina, Endereco, Grade, Parentesco, Hora_aula, Professor, Responsavel, Turma, Username

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Endereco) 
admin.site.register(Grade) 
admin.site.register(Parentesco) 
admin.site.register(Hora_aula)
admin.site.register(Professor)
admin.site.register(Responsavel)
admin.site.register(Turma)
admin.site.register(Username)