from django import forms
from myapp.models.auth_user import Username
from myapp.models.turma import Turma
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), strip=False, widget=forms.PasswordInput, help_text=_("Repita a senha para verificação."))

    class Meta:
        model = Username
        fields = ('password1', 'password2', 'nome', 'turma')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
