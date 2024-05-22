from django.db import connection
from django.views.generic import ListView
from django.shortcuts import render, redirect
from myapp.models.export_models import Turma, Grade, Hora_aula, Disciplina
from django.db.models import F, Value as V, CharField, Case, When, Max, Q
from django.db.models.functions import Concat, Coalesce
from django.http import JsonResponse
#from django.forms import AvisoForm

def home(request):
    return render(request, 'home/home.html')

def turmas(request):
    items = Turma.objects.all()
    return render(request, 'turmas/home.html', {"turmas": items})

def turmas_grade(request, slug):
    splited_slug = slug.split('-')
    turma_ano = splited_slug[0]
    turma_nome = splited_slug[1]

    raw_query = f"""
           SELECT
  CONCAT(
    TO_CHAR(x4.horario_inicial, 'HH24:MI'),
    ' - ',
    TO_CHAR(x4.horario_final, 'HH24:MI')
  ) AS "Horário",
  MAX(
    CASE
      WHEN x4.dia_semana = 'Segunda-feira' THEN COALESCE(x2.disciplina, 'No Subject')
    END
  ) AS "Segunda-feira",
  MAX(
    CASE
      WHEN x4.dia_semana = 'Terça-feira' THEN COALESCE(x2.disciplina, 'No Subject')
    END
  ) AS "Terça-feira",
  MAX(
    CASE
      WHEN x4.dia_semana = 'Quarta-feira' THEN COALESCE(x2.disciplina, 'No Subject')
    END
  ) AS "Quarta-feira",
  MAX(
    CASE
      WHEN x4.dia_semana = 'Quinta-feira' THEN COALESCE(x2.disciplina, 'No Subject')
    END
  ) AS "Quinta-feira",
  MAX(
    CASE
      WHEN x4.dia_semana = 'Sexta-feira' THEN COALESCE(x2.disciplina, 'No Subject')
    END
  ) AS "Sexta-feira"
FROM
  myapp_hora_aula AS x4
  LEFT JOIN myapp_grade AS x1 ON x4.id = x1.hora_aula_id
  LEFT JOIN myapp_disciplina AS x2 ON x2.id = x1.disciplina_id
  LEFT JOIN myapp_turma AS x3 ON x3.id = x1.turma_id
WHERE
  x2.disciplina IS NOT NULL
  AND x3.nome = '{turma_nome}'
  AND x3.ano = '{turma_ano}'
GROUP BY
  CONCAT(
    TO_CHAR(x4.horario_inicial, 'HH24:MI'),
    ' - ',
    TO_CHAR(x4.horario_final, 'HH24:MI')
  )
ORDER BY
  "Horário";
"""

    with connection.cursor() as cursor:
            cursor.execute(raw_query)
            results = cursor.fetchall()
    grade_list = list(results)
    turma = turma_ano+"°"+turma_nome
    print(turma)

    # Render the template with the schedule data
    return render(request, 'grade/index.html', {"grade": grade_list,"turma": turma})


def nova_turma(request):
    if request.method == 'POST':
        # salvar os dados da tela para o banco
        nova_turma = Turma()
        nova_turma.nome = request.POST.get('nome')
        nova_turma.ano = request.POST.get('ano')
        nova_turma.save()

        return redirect('turmas')
    
    return render(request, 'turmas/nova_turma.html')

def editar_turma(request, id):
    turma = Turma.objects.get(pk=id)

    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        turma.ano = request.POST.get('ano')
        turma.save()

        return redirect('turmas')
    
    return render(request, 'turmas/editar_turma.html', {'turma': turma})

def excluir_turma(request, id):
    turma = Turma.objects.get(pk=id)
    turma.delete()
    return redirect('turmas')

def horarios(request):
    items = Hora_aula.objects.all()
    return render(request, 'horarios/home.html', {"horarios": items})

def novo_horario(request):
    if request.method == 'POST':
        # salvar os dados da tela para o banco
        novo_horario = Hora_aula()
        novo_horario.dia_semana = request.POST.get('dia_semana')
        novo_horario.horario_inicial = request.POST.get('horario_inicial')
        novo_horario.horario_final = request.POST.get('horario_final')
        novo_horario.save()

        # return redirect('horarios')
    
    return render(request, 'horarios/novo_horario.html')

def editar_horario(request, id):
    horario = Hora_aula.objects.get(pk=id)
    print(horario.horario_final)

    if request.method == 'POST':
        horario.dia_semana = request.POST.get('dia_semana')
        horario.horario_inicial = request.POST.get('horario_inicial')
        horario.horario_final = request.POST.get('horario_final')
        horario.save()

        return redirect('horarios')
    
    return render(request, 'horarios/editar_horario.html', {'horario': horario})

def excluir_horario(request, id):
    horario = Hora_aula.objects.get(pk=id)
    horario.delete()
    return redirect('horarios')
  
def avisos(request):
   return render(request, 'avisos/avisos.html')
 
 
 #def enviar_notificacao(request):
  #  if request.method == 'POST':
   #     form = NotificacaoForm(request.POST)
    #    if form.is_valid():
     #       form.save()                # para salvar a notificação enviada no bd
      #      messages.success(request, 'Sua notificação foi enviada')
       #     return render(request, 'avisos/avisos.html', {'form': form})
  
def disciplina(request):
    items = Disciplina.objects.all().order_by('id')
    return render(request, 'disciplina/disciplina.html', {"disciplina": items})
  
def nova_disciplina(request):
    if request.method == 'POST':
        nova_disciplina = Disciplina()
        nova_disciplina.disciplina = request.POST.get('disciplina')
        nova_disciplina.save()

        return redirect('disciplina')
    
    return render(request, 'disciplina/nova_disciplina.html')

def editar_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)

    if request.method == 'POST':
        disciplina.disciplina = request.POST.get('disciplina')
        disciplina.save()

        return redirect('disciplina')
    
    return render(request, 'disciplina/editar_disciplina.html', {'disciplina': disciplina})

def excluir_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    disciplina.delete()
    return redirect('disciplina')