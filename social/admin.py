from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Valido si el usuario conectado pertenece al grupo "Personal", no dejo editar los campos 'created', 'updated', 'key', 'name'
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)
