from django.db import models
from django.utils.timezone import now #Para utilizar fechas
from django.contrib.auth.models import User # importo la clase usuario para utilizarla como clave foránea.
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        # Se ordena por el campo "created" del mas nuevo al mas antiguo.
        ordering = ['-created']

    # Permite definir el nombre que se muestra en el panel de administración.
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    # El campo se actualiza al momento de crar un registro, utilizando la zona horaria.
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now) 
    # upload_to: permite almacenar los archivos en la carpeta "blog" dentro de la carpeta "media", puede contener valores nulos.
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # Campo relacionado del modelo User (gestionado por django), si se elimina un usuario, se elimina por cascada sus post realizados.
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    # Campo de relacion de muchos a muchos, le paso como primer parámetro el modelo "Category"
    # El tercer parámetro (related_name) es el nombre para acceder a los post desde una categoría.
    categories = models.ManyToManyField(Category, verbose_name="Categoría", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        # Se ordena por el campo "created" del mas nuevo al mas antiguo.
        ordering = ['-created']

    # Permite definir el nombre que se muestra en el panel de adminitración.
    def __str__(self):
        return self.title
