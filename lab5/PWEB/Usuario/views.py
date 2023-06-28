from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

def login_U(request):
    if request.method == "POST" :
        nombre=request.POST['username']
        contraseña=request.POST['password']
        usuario=authenticate(request,username=nombre,password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return redirect('Inicio')
        else:
            messages.success(request, "Ocurrio -- Erro -- 403")
            return redirect('Login')
    else:
        return render(request, "login.html",{})

def logout_U(request):
    logout(request)
    return redirect('Login')