from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path("", views.home, name="home"),
    path("turmas/", views.turmas, name="turmas"),
    path("turmas/nova_turma", views.nova_turma, name="nova_turma"),
    path('editar/<int:id>/', views.editar_turma, name='editar_turma'),
    path('excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path("avisos/", views.avisos, name="avisos"),
    path("disciplina/", views.disciplina, name="disciplina"),
    path("disciplina/nova_disciplina", views.nova_disciplina, name="nova_disciplina"),
    path("disciplina/editar/<int:id>/", views.editar_disciplina, name="editar_disciplina"),
    path('disciplina/excluir/<int:id>/', views.excluir_disciplina, name='excluir_disciplina'),
    path("horarios/", views.horarios, name="horarios"),
    path("horarios/novo_horario", views.novo_horario, name="novo_horario"),
    path('horarios/editar_horario/<int:id>/', views.editar_horario, name='editar_horario'),
    path('excluir_horario/<int:id>/', views.excluir_horario, name='excluir_horario'),
    path("grade/<int:ano>-<str:nome>/", views.turmas_grade, name="grade"),
]