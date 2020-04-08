from django.contrib import admin
from .models import Category, Post
# Register your models here.

# Permite redefinir configuraciones en el modelo, en este caso de definen los campos "created" y "updated" solo de lectura.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
