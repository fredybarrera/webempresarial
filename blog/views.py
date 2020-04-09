from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

# Obtiene el parametro "category_id" desde la url
def category(request, category_id):
    # Permite obtener registros filtrando por un atributo
    # category = Category.objects.get(id=category_id)

    # Permite buscar y obtener el registro, en caso contrario, muestra error 404
    category = get_object_or_404(Category, id=category_id)

    return render(request, "blog/category.html", {'category': category})