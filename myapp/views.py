from django.shortcuts import render, redirect
from myapp.models.export_models import Turma

def home(request):
    return render(request, 'home/home.html')

def turmas_home(request):
    items = Turma.objects.all()
    return render(request, 'turmas/home.html', {"turmas": items})

def turmas(request):
    if request.method == 'POST':
        nova_turma = Turma(
            nome = request.POST.get('nome'),
            periodo = request.POST.get('periodo'),
            num_sala = request.POST.get('num_sala')
        )
        nova_turma.save()
        
        return redirect('alunos')

    turmas = {
        'turmas': Turma.objects.all()
    }

    return render(request, 'turmas/home.html', turmas)

def editar_turma(request, id):
    turma = Turma.objects.get(pk=id)
    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        turma.periodo = request.POST.get('periodo')
        turma.num_sala = request.POST.get('num_sala')
        turma.save()

        return redirect('turmas')
    
    return render(request, 'turmas/editar_turma.html', {'turma': turma})

def excluir_turma(request, id):
    turma = Turma.objects.get(pk=id)
    turma.delete()
    return redirect('turmas')