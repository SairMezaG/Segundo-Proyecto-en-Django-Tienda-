from django.shortcuts import render
""" from appTienda.models import Categoria """

# Create your views here.


from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')


def vistaCategorias(request):
    return render(request, "formularioCategoria.html")


""" def agregarCategoria(request):
    nombre = request.POST["nombre"]
    try:
        categoria = Categoria(catNombre= nombre)
        categoria.save()
        mensaje = "Categoria agregada correctamente"
    except:
        mensaje = "No se pudo agregar la categoria" 
    retorno = mensaje = mensaje
    return render(request, "formularioCategoria,html", retorno)        """