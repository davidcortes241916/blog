from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


#para usar las opciones de la dependencia
class CategoriaResources(resources.ModelResource):
    class Meta:
        model= Categoria

class AutorResources(resources.ModelResource):
    class Meta:
        model= Autor

#para listar los atributos y sus valores correspondientes
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nombre'] #barra de busqueda
    list_display= ('nombre','estado', 'fecha_creacion') #es una tupla con los atributos que queremos ver
    resource_class= CategoriaResources

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nombres', 'apellidos', 'email']
    list_display= ('nombres', 'apellidos', 'email', 'estado', 'fecha_creacion')
    resource_class= AutorResources

# Register your models here.
#este puede recibir dos parametros, el obligatorio que es la clase del modelo, el opcional es una clase que herede de clase modeladmin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)