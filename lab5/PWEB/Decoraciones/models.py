from django.db import models

# Create your models here.

class Pedido(models.Model):
    NombreC = models.CharField(null=True, max_length=50)
    ApellidosC = models.CharField(null=True, max_length=50)
    telefono = models.IntegerField(null=True)
    Correo = models.EmailField(max_length=254, default='')
    direccion=models.CharField(max_length=50)
    fecha=models.DateField()

class Producto (models.Model):
    nombre=models.CharField(max_length=25)
    descripcion=models.TextField()
    precio=models.CharField(max_length=25)

    class Meta:
        abstract = True

class catalogo(Producto):
    imagen=models.ImageField(null=True,blank=True,upload_to="img/")
class Lista (Producto):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

class Carrito (Producto):
    adquirido = models.BooleanField()
    rutaI = models.CharField(null=True, max_length=50000)