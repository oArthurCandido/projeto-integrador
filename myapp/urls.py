from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home" ),
    path("turmas/", views.turmas, name="turmas" ),
    path("turmas/nova_turma", views.nova_turma, name="nova_turma" ),
    path('editar/<int:id>/', views.editar_turma, name='editar_turma'),
    path('excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path("grade/<slug:slug>", views.turmas_grade, name= "grade" )    
]