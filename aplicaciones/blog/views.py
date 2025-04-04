from django.shortcuts import render
from .models import *
from django.shortcuts import get_list_or_404 
from django.db.models import Q #es para la busqueda, hace que todo se englobe
from django.core.paginator import Paginator #esta libreria sirve para hacer paginacion 

# Create your views here.
def home(request):
    queryset= request.GET.get("buscar") #es el name id que tiene el buscador
    posts= Post.objects.filter(estado=True)
    if queryset:
        posts=Post.objects.filter(
            Q(titulo__icontains= queryset) | Q(descripcion__icontains= queryset)
        ).distinct()

    paginator= Paginator(posts, 2)
    page= request.GET.get("page")
    posts= paginator.get_page(page) #se reescribe la variable por la paginacion

    return render(request, './index.html', {'posts':posts})

def detallePost(request,slug): #el slug es el que esta en model, es donde tendremos acceso para cambiar nuestro id para tener mas informacion de nuestro post
    post= Post.objects.get(
        slug= slug
    )
    print(post)
    
    return render(request, './post.html', {'post':post})

def generales(request):
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact ='generales'))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains= queryset) | Q(descripcion__icontains= queryset),
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact= 'generales'), 
        ).distinct()

    paginator= Paginator(posts, 2)
    page= request.GET.get("page")
    posts= paginator.get_page(page)

    return render(request, './generales.html', {'posts':posts})

def programacion(request):
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact ='programacion'))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains= queryset) | Q(descripcion__icontains= queryset),
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact= 'generales'), 
        ).distinct()

    paginator= Paginator(posts, 2)
    page= request.GET.get("page")
    posts= paginator.get_page(page)

    return render(request, './programacion.html', {'posts':posts})

def tutoriales(request):
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact ='tutoriales'))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains= queryset) | Q(descripcion__icontains= queryset),
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact= 'generales'), 
        ).distinct()
    
    paginator= Paginator(posts, 2)
    page= request.GET.get("page")
    posts= paginator.get_page(page)
    
    return render(request, './tutoriales.html',{'posts':posts})