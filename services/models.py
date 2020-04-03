from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    # upload_to: permite almacenar los archivos en la carpeta "services" dentro de la carpeta "media"
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    # Campo de fecha y hora (timestamp). Se ejecuta cuando se guarda un registro
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # Campo de fecha y hora (timestamp). Se ejecuta cuando se actualiza in registro
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        # Se ordena por el campo "created" del mas nuevo al mas antiguo.
        ordering = ['-created']

    # Permite definir el nombre que se muestra en el panel de adminitración.
    def __str__(self):
        return self.title
