from django.urls import path
from . import views

urlpatterns = [
    # Para pasar por parámetro un id
    # se parsea el parámetro a entero
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"),
]
