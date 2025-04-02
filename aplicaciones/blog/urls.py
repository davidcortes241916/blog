from django.urls import path
from .views import *
#la otra forma es
#from . improt views

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name="generales"),
    path('programacion/', programacion, name="programacion"),
    path('tutoriales/', tutoriales, name="tutoriales"),
]