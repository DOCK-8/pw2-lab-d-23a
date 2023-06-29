from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Producto (models.Model):
    imagen=models.ImageField(null=True,blank=True,upload_to="img/")
    nombre=models.CharField(max_length=25)
    descripcion=models.TextField()
    precio=models.IntegerField()
class Pedido(models.Model):
    NombreC = models.CharField(null=True, max_length=50)
    ApellidosC = models.CharField(null=True, max_length=50)
    telefono = models.IntegerField(null=True)
    Correo = models.EmailField(max_length=254, default='')
    direccion=models.CharField(max_length=50)
    fecha=models.DateField()
    productos = models.ManyToManyField(Producto)

