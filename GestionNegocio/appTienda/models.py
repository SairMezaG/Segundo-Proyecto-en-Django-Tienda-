from django.db import models

# Create your models here.


class Categoria(models.Model):
    catNombre = models.CharField(max_length=50, unique=True)



"""  prodFoto = models.ImageField(upload_to="fotos/", null=True, blank=True)   Investigar la diferencia"""
class Producto(models.Model):
    prodCodigo= models.IntegerField(unique=True)
    prodNombre= models.CharField(max_length=50)
    prodPrecio= models.IntegerField()
    prodCategoria= models.ForeignKey(Categoria, on_delete=models. PROTECT)
    prodFoto = models.FileField(upload_to="fotos/", null=True, blank=True)
   
   

