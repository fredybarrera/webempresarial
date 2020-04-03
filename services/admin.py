from django.contrib import admin
from .models import Service
# Register your models here.

# Permite redefinir configuraciones en el modelo, en este caso de definen los campos "created" y "updated" solo de lectura.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)