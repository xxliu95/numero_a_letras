from django.shortcuts import render, redirect
from .models import Texto
from .forms import Entrada
from .utils import numero_a_letras

def mi_vista(request):
    form = Entrada()
    resultado = None

    if request.method == "POST":
        form = Entrada(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            resultado = numero_a_letras(numero)

    return render(request, 'app/index.html', {'form': form, 'resultado': resultado})
