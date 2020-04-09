from .models import Link
# Extiendo el diccionario de cotexto.
def ctx_dict(request):
    ctx = {}
    # Obtengo los links y los guardo con su clave y url dentro de la variable ctx
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx