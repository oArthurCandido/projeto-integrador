#from django import forms
##from django.models import Turma >> após ajustar campo turma no formulário

#class AvisoForm(forms.ModelForm):
#    identificacao = forms.CharField(label='Identificação', widget=forms.TextInput(attrs={'placeholder': 'Escola ou nome do professor'}))
 #   turma = forms.CharField(label='Turma', widget=forms.TextInput(attrs={'placeholder': 'Selecione a turma'}))
  #  #forms.ModelChoiceField(label='Turma',queryset=Turma.objects.all()) >>> para puxar do bd mas falta checar nome correto considerando mostrar as séries 6a, 7a etc
   # aviso = forms.CharField(label='Aviso', widget=forms.Textarea(attrs={'placeholder': 'Escreva a notificação aqui'}))