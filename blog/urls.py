from django.urls import path
from . import views

urlpatterns = [
    # Paths services
    path('', views.blog, name="blog"),
    # Para pasar por parámetro un id
    # se parsea el parámetro a entero
    path('category/<int:category_id>/', views.category, name="category"),
]
