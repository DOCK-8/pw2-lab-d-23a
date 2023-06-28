from django.shortcuts import render
from Decoraciones.models import Producto
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
#Pagina de Inicio
def Home(request):
    list_producto=Producto.objects.all()
    return render(request,"home.html",{"producs":list_producto})
def Bebidas(request):
    return render(request,"Bbs.html")
def Bocaditos(request):
    return render(request,"Bts.html")
def Equipos(request):
    return render(request,"Eps.html")
def Decoraciones(request):
    return render(request,"Dec.html")