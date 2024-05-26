from django import forms
from .models import db, Usuari, Rol

class UsuariForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ['nom', 'cognom', 'assignatures', 'rol']
