from django.db import models

# Create your models here.
class Imagen (models.Model):
    url=models.CharField()
    mombre=models.CharField()
    descripcion=models.CharField()
class Cliente (models.Model):
    nombre=models.CharField()
    correo=models.EmailField()
class Pedido(models.Model):
    estado=models.BooleanField()
    direccion=models.CharField()
    precio=models.DecimalField()
    fecha=models.DateField()

