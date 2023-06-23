from django.shortcuts import render

# Create your views here.
#Pagina de Inicio
def Home(request):
    return render(request,"home.html")
def Bebidas(request):
    return render(request,"Bbs.html")
def Bocaditos(request):
    return render(request,"Bts.html")
def Equipos(request):
    return render(request,"Eps.html")
def Decoraciones(request):
    return render(request,"Dec.html")