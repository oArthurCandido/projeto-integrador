from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="Home" ),
    path("turmas/", views.turmas_home, name="Turmas" ),
    path("grade/<slug:slug>", views.turmas_grade, name= "Grade" )    
]