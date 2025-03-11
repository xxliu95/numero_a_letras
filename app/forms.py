from django import forms
from .models import Texto

class Entrada(forms.ModelForm):
    class Meta:
        model = Texto
        fields = ['numero']

    def __init__(self, *args, **kwargs):
        super(Entrada, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
