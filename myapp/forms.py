from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Agenda, Hora_aula, Disciplina, Turma
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
    class Meta:
        model = Agenda
        fields = '__all__'
 
 