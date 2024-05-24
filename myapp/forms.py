from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hora_aula, Disciplina, Turma
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.contrib.auth.models import Group

    
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Usuário")
    email = forms.EmailField(label="Endereço de email")
    password1 = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Senha confirmação", strip=False, widget=forms.PasswordInput, help_text=_("Repita a senha para verificação."))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

class AgendaForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=Turma.objects.all())
    horario_segunda = forms.ModelChoiceField(queryset=Hora_aula.objects.all(), label='Horário Segunda-feira')
    disciplina_segunda = forms.ModelChoiceField(queryset=Disciplina.objects.all(), label='Disciplina Segunda-feira')
    horario_terca = forms.ModelChoiceField(queryset=Hora_aula.objects.all(), label='Horário Terça-feira')
    disciplina_terca = forms.ModelChoiceField(queryset=Disciplina.objects.all(), label='Disciplina Terça-feira') 
    horario_quarta = forms.ModelChoiceField(queryset=Hora_aula.objects.all(), label='Horário Quarta-feira')
    disciplina_quarta = forms.ModelChoiceField(queryset=Disciplina.objects.all(), label='Disciplina Quarta-feira')
    horario_quinta = forms.ModelChoiceField(queryset=Hora_aula.objects.all(), label='Horário Quinta-feira')
    disciplina_quinta = forms.ModelChoiceField(queryset=Disciplina.objects.all(), label='Disciplina Quinta-feira')
    horario_sexta = forms.ModelChoiceField(queryset=Hora_aula.objects.all(), label='Horário sexta-feira')
    disciplina_sexta = forms.ModelChoiceField(queryset=Disciplina.objects.all(), label='Disciplina Sexta-feira')

    class Meta:
        model = Hora_aula
        fields = ['turma', 'horario_segunda', 'disciplina_segunda', 'horario_terca', 'disciplina_terca', 'horario_quarta', 'disciplina_quarta', 'horario_quinta', 'disciplina_quinta', 'horario_sexta', 'disciplina_sexta']