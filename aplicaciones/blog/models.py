from django.db import models
from ckeditor.fields import RichTextField #se ve asi como si no fuera una libreria

# Create your models here.
class Categoria(models.Model):
    id= models.AutoField(primary_key = True)
    nombre= models.CharField('Nombre de la categoria', max_length=100, null=False, blank=False)
    estado= models.BooleanField('Categoria activada/Categoria no activada', default=True)
    fecha_creacion= models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name= 'Categoria' #es la manera de identificar cada que se mencione de manera individual
        verbose_name_plural= 'Categorias' #es cuando se mencione en plural 

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    nombres= models.CharField('Nombres de Autor', max_length=255, null=False, blank=False)
    apellidos= models.CharField('Apellidos de Autor', max_length=255, null=False, blank=False)
    facebook= models.URLField('Facebook', max_length=200, null=True, blank=True)
    Instagram= models.URLField('Instagram', max_length=200, null=True, blank=True)
    twitter= models.URLField('twitter', max_length=200, null=True, blank=True)
    web= models.URLField('web', max_length=200, null=True, blank=True)
    email= models.EmailField('Correo Electronico', max_length=254, null=False, blank=False)
    estado= models.BooleanField('Autor activo/No activo', default=True) #para la eliminacion logica
    fecha_creacion= models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name= 'Autor' 
        verbose_name_plural= 'Autores'

    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)
    
class Post(models.Model):
    id= models.AutoField(primary_key=True)
    titulo= models.CharField('titulo', max_length=90, null=False, blank=False)
    slug= models.CharField('slug', max_length=100, null=False, blank=False)#es para acceder a cada instancia de nuestro modelo post
    descripcion= models.CharField('descripcion', max_length=110, null=False, blank=False)
    contenido= RichTextField('contenido')
    imagen= models.URLField(max_length=255, null=False, blank=False)#espara poder renderizar las imagines desde internet, para importar desde hiroku, si hay un servidor que permite almacenar imagenes hay si seria un parametro de imagen fields
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado= models.BooleanField('publicado/ no publicado', default=True)
    fecha_creacion= models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name= 'post'
        verbose_name_plural= 'posts'

    def __str__(self):
        return self.titulo