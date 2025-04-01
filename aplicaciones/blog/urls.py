from django.urls import path
from .views import *
#la otra forma es
#from . improt views

urlpatterns = [
    path('', home, name='index'),
]