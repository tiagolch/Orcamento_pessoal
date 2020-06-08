from django.shortcuts import render

def index(request):
    return render(request, 'orcamento/index.html')



def lista_despesas(request):
    return render(request, 'orcamento.lista_despesas.html')