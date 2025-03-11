from django import forms
from .models import Texto

class Entrada(forms.ModelForm):
    class Meta:
        model = Texto
        fields = ['numero']
