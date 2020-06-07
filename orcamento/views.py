from django.shortcuts import render

def index(request):
    return render(request, 'orcamento/index.html')