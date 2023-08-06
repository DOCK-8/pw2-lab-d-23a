from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Sum
from Usuario.forms import FormularioUser,FormularioLogin
from Usuario.models import Usuario
from Decoraciones.models import catalogo,Carrito,Pedido
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, FloatField, Sum

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Decoraciones:Inicio')

    @method_decorator (csrf_protect)
    @method_decorator (never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
    
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

def deshacer_cambio(request, history_id):
    objeto_historial = get_object_or_404(catalogo.historial, history_id=history_id)
    producto = objeto_historial.history_object
    print(objeto_historial.history_object)
    if objeto_historial.get_history_type_display() == "Deleted":
        # Crear un objeto en catalogo para deshacer el cambio de tipo "Deleted"
        nuevo_objeto_catalogo = catalogo.objects.create(
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            precio=producto.precio,
            Categoria=producto.Categoria,
            Estado=producto.Estado,
            imagen=producto.imagen,
            tipo=producto.tipo
        )
        # Eliminar el objeto historial
        print("Restaurando cambio de tipo 'Deleted'")
    elif objeto_historial.get_history_type_display() == "Changed":
        # Restaurar el cambio de tipo "Changed"
        objeto_actual = catalogo.objects.get(id=producto.id)
        objeto_actual.nombre = producto.nombre
        objeto_actual.descripcion = producto.descripcion
        objeto_actual.precio = producto.precio
        objeto_actual.Categoria = producto.Categoria
        objeto_actual.Estado = producto.Estado
        objeto_actual.imagen = producto.imagen
        objeto_actual.tipo = producto.tipo
        objeto_actual.save()
        # Eliminar el objeto historial
        print("Restaurando cambio de tipo 'Changed'")
    else:
        objeto_guardado = catalogo.objects.get(id=producto.id)
        objeto_guardado.delete()
    objeto_historial.delete()
    return redirect('Historial')


# Create your views here.

#Lista de productos.

List_prod=Carrito.objects.all()

class regist_U(CreateView):
    model = Usuario
    form_class = FormularioUser
    template_name = 'registro.html'
    success_url = reverse_lazy('login')
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                userName = form.cleaned_data.get('userName'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('Decoraciones:Inicio')
        else:
            return render(request,self.template_name,{'form':form})
def Proforma(request):

    if request.method == "POST":
        contrato = Pedido(request.POST)
        if contrato.is_valid():
            contrato.save()
            contrato.carrito = Carrito.objects.all()
    else:
        contrato=Pedido()
    return render(request, 'Proforma.html',{"Ped":contrato,"productos":List_prod})

from django.contrib.auth.decorators import login_required

@login_required
def agregar(request):
    if request.method == "POST":
        nombreC = request.POST.get('nombre')
        descripcionC = request.POST.get('descripcion')
        precioC = request.POST.get('precio')
        urlC = request.POST.get('imagen_url')
        cantidad = request.POST.get('cantidad')
        comprador = request.user
        carrito = Carrito(nombre=nombreC, descripcion=descripcionC, precio=precioC, adquirido=True, cantidad=cantidad, rutaI=urlC, comprador=comprador)
        carrito.save()

    return redirect("Decoraciones:Inicio")

def borrar(request, numero):
    articulo = Carrito.objects.get(id=numero)
    articulo.delete()
    return redirect("usuario:bolsa")

from django.db.models import F, Sum

def lista(request):
    listaArticulo = Carrito.objects.all()
    total = listaArticulo.aggregate(total=Sum(F('precio') * F('cantidad')))['total'] or 0
    return render(request, 'lista.html', {"productos": listaArticulo, "total": total})


@login_required
def download_pdf(request):
    usuario = request.user.userName
    productos = Carrito.objects.filter(comprador=request.user)
    total = sum(producto.precio * producto.cantidad for producto in productos)
    
    # Renderizar el contenido del PDF usando el archivo de plantilla HTML
    html_content = render_to_string('pdf.html', {'usuario': usuario, 'productos': productos, 'total': total})
        
    # Convertir el contenido HTML a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    pisa.CreatePDF(html_content, dest=response)
    
    return response
