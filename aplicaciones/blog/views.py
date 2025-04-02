from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    posts= Post.objects.filter(estado=True)
    return render(request, './index.html', {'posts':posts})

def generales(request):
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre ='generales'))
    return render(request, './generales.html', {'posts':posts})

def programacion(request):
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre ='programacion'))
    return render(request, './programacion.html', {'posts':posts})

def tutoriales(request):
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre ='tutoriales'))
    return render(request, './tutoriales.html',{'posts':posts})