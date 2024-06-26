from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('sign_up', views.sign_up, name='sign_up'),
    path("", views.home, name="home"),
    path("turmas/", views.turmas, name="turmas"),
    path("turmas/nova_turma", views.nova_turma, name="nova_turma"),
    path('editar/<int:id>/', views.editar_turma, name='editar_turma'),
    path('excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path("avisos/", views.enviar_notificacao, name="avisos"),
    path("disciplina/", views.disciplina, name="disciplina"),
    path("disciplina/nova_disciplina", views.nova_disciplina, name="nova_disciplina"),
    path("disciplina/editar/<int:id>/", views.editar_disciplina, name="editar_disciplina"),
    path('disciplina/excluir/<int:id>/', views.excluir_disciplina, name='excluir_disciplina'),
    path("horarios/", views.horarios, name="horarios"),
    path("horarios/novo_horario", views.novo_horario, name="novo_horario"),
    path('horarios/editar_horario/<int:id>/', views.editar_horario, name='editar_horario'),
    path('excluir_horario/<int:id>/', views.excluir_horario, name='excluir_horario'),
    path("grade/<int:ano>-<str:nome>/", views.turmas_grade, name="grade"),
    path("agenda/", views.agenda, name="agenda"),
    path("agenda/nova_agenda", views.nova_agenda, name="nova_agenda"),
    path("agenda/editar/<int:id>/", views.editar_agenda, name="editar_agenda"),
    path("agenda/excluir/<int:id>/", views.editar_agenda, name="excluir_agenda"),
    path("user_turma", views.user_turma, name="user_turma"),
    path("user_turma/adicionar_turma/<int:id>", views.adicionar_turma, name="adicionar_turma"),
    path('user_turma/editar/<int:user_turma_id>/', views.editar_user_turma, name='editar_user_turma'),
    path('user_turma/excluir/<int:user_turma_id>/', views.excluir_user_turma, name="user_turma"),
 #   path('agenda/<int:turma_id>/', views.agenda, name='agenda'),
]