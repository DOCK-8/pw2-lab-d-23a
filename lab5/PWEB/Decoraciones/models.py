from django.db import models

# Create your models here.
class Producto (models.Model):
    imagen=models.ImageField(null=True,blank=True,upload_to="img/")
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150)
    precio=models.IntegerField()
class Cliente (models.Model):
    nombre=models.CharField(max_length=20)
    correo=models.EmailField(max_length=30)
class Pedido(models.Model):
    estado=models.BooleanField()
    direccion=models.CharField(max_length=50)
    fecha=models.DateField()

