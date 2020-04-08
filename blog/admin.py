from django.contrib import admin
from .models import Category, Post
# Register your models here.

# Permite redefinir configuraciones en el modelo, en este caso de definen los campos "created" y "updated" solo de lectura.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    # Puedo hacer busquedas dentro de autor por el campo "username".
    # Busco ademas por los nombres de las categorias.
    search_fields = ('title', 'content', 'author__username', 'categories__name') 
    # Permite jerarquizar por fechas.
    date_hierarchy = 'published'
    # Permite añadir filtros de búsqueda
    list_filter = ('author__username', 'categories__name')
    
    # Permite definir lo que se mostrará en la columna, en este caso son los nombres de las categorias separados por coma (,)
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    # Sobreescribe el atributo 'short_description' para agregar un texto mas descriptivo.
    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
