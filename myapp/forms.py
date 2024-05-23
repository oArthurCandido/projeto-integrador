from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models.auth_user import Username
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Username
        fields = ('nome', 'turma')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
