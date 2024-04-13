from django.contrib import admin
from myapp.models.export_models import Aluno, Disciplina, Endereco,Grade, Parentesco, Periodo, Professor, Responsavel, Turma


# Register your models here.
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Endereco) 
admin.site.register(Grade) 
admin.site.register(Parentesco) 
admin.site.register(Periodo)
admin.site.register(Professor)
admin.site.register(Responsavel)
admin.site.register(Turma)
