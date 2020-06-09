from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'orcamento/index.html')



def lista_despesas(request):

    lista = despesas.objects.all()

    dados = {'despesas': lista}
    return render(request, 'orcamento/lista_despesas.html', dados)