from django.db import models

# Create your models here.
class Imagen (models.Model):
    url=models.CharField(max_length=50)
    mombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150)
class Cliente (models.Model):
    nombre=models.CharField(max_length=20)
    correo=models.EmailField(max_length=30)
class Pedido(models.Model):
    estado=models.BooleanField()
    direccion=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    fecha=models.DateField()

