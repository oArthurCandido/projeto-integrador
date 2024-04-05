from django.urls import path
from myapp import views

urlpatterns = [
    path('turmas/', views.turmas, name='turmas')
]
