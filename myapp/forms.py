from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Turma

#class AvisoForm(forms.ModelForm):
#    identificacao = forms.CharField(label='Identificação', widget=forms.TextInput(attrs={'placeholder': 'Escola ou nome do professor'}))
 #   turma = forms.CharField(label='Turma', widget=forms.TextInput(attrs={'placeholder': 'Selecione a turma'}))
  #  #forms.ModelChoiceField(label='Turma',queryset=Turma.objects.all()) >>> para puxar do bd mas falta checar nome correto considerando mostrar as séries 6a, 7a etc
   # aviso = forms.CharField(label='Aviso', widget=forms.Textarea(attrs={'placeholder': 'Escreva a notificação aqui'}))
   
#class CustomUserCreationForm(UserCreationForm):
 #   class Meta:
  #      model = User
   #     fields = ('username', 'email', 'password1', 'password2')
    #    labels = {
     #       'username': _('Nome de usuário'),
      #      'email': _('Email'),
       #     'password1': _('Senha'),
        #    'password2': _('Confirme a senha'),
#        }
 #       help_texts = {
  #          'username': _('Apenas letras ou números'),
   #         'password1': _('Sua senha deve conter pelo menos 8 caracteres.'),
    #        'password2': _('Digite a mesma senha novamente para verificação.'),
     #   }
      #  error_messages = {
       #     'username': {
        #        'unique': _("Um usuário com esse nome já existe."),
         #   },
      #    #  'password_mismatch': _("As senhas não coincidem."),
      #  }
        
class CustomUserCreationForm(UserCreationForm):
    turmas = forms.ModelMultipleChoiceField(queryset=Turma.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'turmas')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.turmas.set(self.cleaned_data['turmas'])
            user_profile.save()
        return user
