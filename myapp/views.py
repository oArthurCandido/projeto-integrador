from django.db import connection
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models.export_models import Turma, Grade, Hora_aula, Disciplina, Horario, Agenda, User_Turma
from django.db.models import F, Value as V, CharField, Case, When, Max, Q
from django.db.models.functions import Concat, Coalesce
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, AgendaForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
#from django.forms import AvisoForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request,'grade.index.html')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('home') 
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def home(request):
    return render(request, 'home/home.html')
    
    adicionar_turma
@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def adicionar_turma(request, id):
    user = User.objects.get(pk=id)
    turmas = Turma.objects.all()

    if request.method == 'POST':
        turma = Turma.objects.get(pk=request.POST.get('turma_id'))
        user_turma = User_Turma()
        user_turma.user = user
        user_turma.turma = turma
        user_turma.save()

        return redirect('user_turma')
    
    return render(request, 'user_turma/adicionar_turma.html', {"turmas": turmas})

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def user_turma(request):    
    raw_query = f"""
        SELECT
            u.id as user_id,
            u.username as username,
            concat( t.ano,
                '-',
                t.nome) as turma
        FROM
            auth_user AS u LEFT JOIN myapp_user_turma AS ut ON ut.user_id = u.id
            LEFT JOIN myapp_turma AS t ON ut.turma_id = t.id
        WHERE
            u.is_superuser = 'FALSE'
    """

    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        results = cursor.fetchall()
        user_turmas = list(results)

    return render(request, 'user_turma/home.html', {"user_turmas": user_turmas})

@login_required(login_url='/login') 
@user_passes_test(lambda u: u.is_superuser)
def turmas(request):
    items = Turma.objects.all()
    return render(request, 'turmas/home.html', {"turmas": items})

@login_required(login_url='/login')
def turmas_grade(request, ano, nome):
    splited_slug = f"{ano}-{nome}".split('-')
    turma_ano = splited_slug[0]
    turma_nome = splited_slug[1]

    user = request.user

    raw_user_query = f"""
        SELECT
            ut.user_id,
            t.ano,
            t.nome
        FROM
            myapp_user_turma AS ut
            LEFT JOIN myapp_turma AS t ON ut.turma_id = t.id
        WHERE
            ut.user_id = {user.id}
            AND t.nome = '{turma_nome}'
            AND t.ano = '{turma_ano}'
    """

    with connection.cursor() as cursor:
        cursor.execute(raw_user_query)

    if user.is_superuser or cursor.rowcount > 0 :
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
        
    else:
        grade_list = []

    turma = turma_ano + "°" + turma_nome
    print(turma)
    return render(request, 'grade/index.html', {"grade": grade_list, "turma": turma})

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def nova_turma(request):
    if request.method == 'POST':
        nova_turma = Turma()
        nova_turma.nome = request.POST.get('nome')
        nova_turma.ano = request.POST.get('ano')
        nova_turma.save()

        return redirect('turmas')
    
    return render(request, 'turmas/nova_turma.html')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def editar_turma(request, id):
    turma = Turma.objects.get(pk=id)
    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        turma.ano = request.POST.get('ano')
        turma.save()

        return redirect('turmas')
    
    return render(request, 'turmas/editar_turma.html', {'turma': turma})

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def excluir_turma(request, id):
    turma = Turma.objects.get(pk=id)
    turma.delete()
    return redirect('turmas')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def horarios(request):
    items = Hora_aula.objects.all()
    return render(request, 'horarios/home.html', {"horarios": items})


@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def novo_horario(request):
    if request.method == 'POST':
        novo_horario = Hora_aula()
        novo_horario.dia_semana = request.POST.get('dia_semana')
        novo_horario.horario_inicial = request.POST.get('horario_inicial')
        novo_horario.horario_final = request.POST.get('horario_final')
        novo_horario.save()
        # return redirect('horarios')
    
    return render(request, 'horarios/novo_horario.html')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
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

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def excluir_horario(request, id):
    horario = Hora_aula.objects.get(pk=id)
    horario.delete()
    return redirect('horarios')
  
@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def avisos(request):
   return render(request, 'avisos/avisos.html')
 
 #def enviar_notificacao(request):
  #  if request.method == 'POST':
   #     form = NotificacaoForm(request.POST)
    #    if form.is_valid():
     #       form.save()                # para salvar a notificação enviada no bd
      #      messages.success(request, 'Sua notificação foi enviada')
       #     return render(request, 'avisos/avisos.html', {'form': form})
  
@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def disciplina(request):
    items = Disciplina.objects.all().order_by('id')
    return render(request, 'disciplina/disciplina.html', {"disciplina": items})

@login_required(login_url='/login') 
@user_passes_test(lambda u: u.is_superuser)
def nova_disciplina(request):
    if request.method == 'POST':
        nova_disciplina = Disciplina()
        nova_disciplina.disciplina = request.POST.get('disciplina')
        nova_disciplina.save()

        return redirect('disciplina')
    
    return render(request, 'disciplina/nova_disciplina.html')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def editar_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)

    if request.method == 'POST':
        disciplina.disciplina = request.POST.get('disciplina')
        disciplina.save()

        return redirect('disciplina')
    
    return render(request, 'disciplina/editar_disciplina.html', {'disciplina': disciplina})

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def excluir_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    disciplina.delete()
    return redirect('disciplina')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def agenda(request):
    items = Grade.objects.all().order_by('id')
    return render(request, 'agenda/agenda.html', {"agenda": items})

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def editar_agenda(request, id):
    agenda = Hora_aula.objects.get(pk=id)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda-list')
    else:
        form = AgendaForm(instance=agenda)
    return render(request, 'agenda/editar_agenda.html', {'form': form, 'agenda': agenda})

#def excluir_agenda(request, id):
 #   agenda = Hora_aula.objects.get(pk=id)
  #  agenda.delete()
   # return redirect('agenda-list')

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def nova_agenda(request):
    horarios = Hora_aula.objects.filter(dia_semana = 'Segunda-feira')
    disciplinas = Disciplina.objects.all()
    dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']

    if request.method == 'POST':
        for idx, horario in enumerate(horarios[:7]):
            agenda = Agenda(
                horario=horario,
                segunda=Disciplina.objects.get(id=request.POST.get('disciplina_segunda_{idx+1}')),
                terca=Disciplina.objects.get(id=request.POST.get('disciplina_terca_{idx+1}')),
                quarta=Disciplina.objects.get(id=request.POST.get('disciplina_quarta_{idx+1}')),
                quinta=Disciplina.objects.get(id=request.POST.get('disciplina_quinta_{idx+1}')),
                sexta=Disciplina.objects.get(id=request.POST.get('disciplina_sexta_{idx+1}'))
            )
            agenda.save()
        return redirect('agenda-list')

    context = {
        'horarios': horarios,
        'disciplinas': disciplinas,
        'dias': dias
    }
    return render(request, 'agenda/nova_agenda.html', context)


#def listar_series(request):
 #   series = Turma.objects.all()
  #  context = {
   #     'series': series
    #}
    #return render(request, 'agenda.html', context)
