from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView

# Create your views here.

def listarDiscos(request):

    discos = Disco.objects.all()
    return render(request, 'base_lista_discos.html', {'discos': discos})

def detalheDisco(request, pk):

    disco = Disco.objects.get(pk=pk)
    return render(request, 'detalhe_disco.html', {'disco':disco})