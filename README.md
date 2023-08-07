<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para inscripción de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2022/08/09</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>30-May-2022</td><td>FECHA FIN:</td>
        <td>06-Agos-2023</td><td>DURACIÓN:</td><td>1 semestre</td>
    </tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    Consultar una proforma para una fiesta implica obtener información detallada sobre los servicios y productos que se ofrecen para un evento o celebración     específica. Una proforma es un documento que proporciona una descripción completa de los elementos que formarán parte de la fiesta, junto con sus respectivos precios. Esto permite a los clientes tener una idea clara de los costos y los servicios incluidos antes de confirmar la contratación del evento.
##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a traves de una URL.(False)
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.(True)
    - RQ03 : El sistema debe permitir gestionar la publicacion, proformas (pdf-Datos previos)

##  Modelo de datos
    El modelo de datos estan conformados por las siguientes entidades.

    -  Fiesta(models.Model): En esta entidad se almacena la información de la fiesta para la que se, esta desarrollando esta proforma.
    -  Galeria(models.Model): En esta entidad se almacena las imagenes que se utilizaran para los objetos de catalogo.
    -  Tipo(models.Model): En esta entidad se almacena los tipos, a los que pertenece cada objeto del modelo producto.
    -  Distrito(models.Model): En esta entidad se almacena los distritos de la ubicacion de la fiesta.
    -  Asociaciones (models.Model): En esta se especifica la ubicacion (Distrito, asc., mz, lt) de la vivienda-dando mas libertad al usuario para la descripcion.
    -  Producto(models.Model): Es un modelo abstracto, que sirve como guia de estructura para Catalo y Carrito. Guarda caracteristicas, como es el nombre, descripcion, precio, estado y compra, que determinan su estado durante la visita del cliente a la pagina.
    -  catalogo(Producto): Es el modelo hijo de Producto que agrega, una imagen, para la visualizacion en la pagina; y agrega un Tipo(modelo) para                     poder diferenciarlo en las vistas.
    -  Carrito(Producto): Este como almacena un producto, con su respectivo comprador, cantidad para poder sacar una proforma del evento.
    -  Pedido(models.Model): Este almacena un carrito,fecha para poder reconocer el tiempo de plazo hasta la celebracion

##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| FIESTA | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| motivo  | charField | No | Si | Ninguno | Fiesta |

| GALERIA | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| imagen  | imageField | No | Si | Ninguno | Imagen |

| TIPO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Tip  | charField | No | Si | Ninguno | ninguno |

| DISTRITO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| distrito  | CharField | No | Si | Ninguno | Distrito |

| ASOCIACIONES | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Distrito  | Distrito | No | Si | Ninguno | ninguno |
| Asoc  | charField | No | Si | Ninguno | Asociacion - Sector |
| Mz  | charField | No | Si | Ninguno | ninguno |
| Lt  | IntegerField | No | Si | Ninguno | Lote |

| PRODUCTO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| nombre  | charField | No | Si | Ninguno | No |
| descripcion  | textField | No | Si | Ninguno | No |
| precio  | decimalField | No | Si | Ninguno | No |
| Estado  | booleanField | No | Si | True | Activo |
| Compra  | booleanField | No | Si | False | Seleccionado (S/N) |

| CATALOGO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| nombre  | charField | No | No | Ninguno | No |
| descripcion  | textField | No | No | Ninguno | No |
| precio  | decimalField | No | No | Ninguno | No |
| Estado  | booleanField | No | No | True | Activo |
| Compra  | booleanField | No | No | False | Seleccionado (S/N) |
| imagen  | Galeria | No | No | Ninguno | Imagen |
| tipo  | Tipo | Si | No | True | No |

| CARRITO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| nombre  | charField | No | No | Ninguno | No |
| descripcion  | textField | No | No | Ninguno | No |
| precio  | decimalField | No | No | Ninguno | No |
| Estado  | booleanField | No | No | True | Activo |
| Compra  | booleanField | No | No | False | Seleccionado (S/N) |
| comprador  | User | No | No | Ninguno | No |
| adquirido  | booleanField | No | No | Ninguno | Seleccionado (S/N) |
| cantidad  | integerField | No | No | Ninguno | Cantidad: U |
| rutaI  | charField | Si | No | True | No |

| PEDIDO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Entregado  | booleanField | No | No | Ninguno | No |
| direccion  | charField | No | No | Ninguno | No |
| fecha  | dateField | No | No | Ninguno | No |
| Carrito  | Carrito | Si | No | Ninguno | No |

## Diagrama Entidad-Relación
![Diagrama Entidad-Relación](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/erd.png)

##  Administración con Django
Instalacion:
 sudo apt-get install -y python3-pip
 sudo apt install -y python3-venv
Creamos el entorno:
 virtualenv -p python3 .
 source ../bin/activate
Instalacion con PIP:
 pip install Django
 pip install pillow
 pip install djangorestframework
 pip install markdown
 pip install django-filter
Creacion del projecto-django:
 django-admin startproject PWEB
Creacion de la app Decoraciones y Usuario:
 cd PWEB
 python manage.py startapp Decoraciones
 python manage.py startapp Usuario
Configurando el Projecto:
 INSTALLED_APPS = [
     'Usuario',
    'Decoraciones',
    'rest_framework',
                  ]
                    
 REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
                        ]
                }
Desarrollando models -> Decoraciones/model.py:

    class Fiesta(models.Model):
        ...
    class Galeria(models.Model):
        ...
    class Tipo(models.Model):
        ...
    class Distrito(models.Model):
        ...
    class Asociaciones (models.Model):
        ...
    class Producto(models.Model):
        ...
    class catalogo(Producto):
        ...
    class Carrito(Producto):
        ...
    class Pedido(models.Model):
        ...
Desarrollando models -> Usuario/model.py:

    class UsuarioManager(BaseUserManager):
        ...
    class Usuario (AbstractBaseUser):    
        ...
Ejecucion:
![Diagrama Entidad-Relación](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/Img/Captura%20desde%202023-08-06%2019-21-43.png)

Desarrollo de urls -> Decoraciones:
from django.urls import path
from Decoraciones import views
app_name = 'Decoraciones'
urlpatterns = [
    path('', views.Home, name="Inicio"),
    path('Bebidas/', views.Bebidas, name="Bebidas"),
    path('Bocaditos/', views.Bocaditos, name="Bocaditos"),
    path('Equipos/', views.Equipos, name="Equipos"),
    path('Decoraciones/', views.Decoraciones, name="Decoraciones"),
    path('Historial/',views.Historial, name="Historial")
]
Desarrollo de views -> Decoraciones:
from django.shortcuts import render
from Decoraciones.models import catalogo

def Historial(request):
    histories = catalogo.historial.all()
    return render(request, "Historial.html", {'History': histories})
# Lista de elementos
#Pagina de Inicio
def Home(request):
    list_producto=catalogo.objects.all()
    return render(request,"home.html",{"producs":list_producto})
def Bebidas(request):
    list_producto=catalogo.objects.all()
    return render(request,"Bbs.html",{"producs":list_producto})
def Bocaditos(request):
    list_producto=catalogo.objects.all()
    return render(request,"Bts.html",{"producs":list_producto})
def Equipos(request):
    list_producto=catalogo.objects.all()
    return render(request,"Eps.html",{"producs":list_producto})
def Decoraciones(request):
    list_producto=catalogo.objects.all()
    return render(request,"Dec.html",{"producs":list_producto})
Desarrollo de urls -> PWEB:
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static
from Usuario.views import Login,logoutUsuario
from django.contrib.auth.decorators import login_required
from Decoraciones.models import Tipo,Carrito,catalogo

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ['Tip']

# ViewSets define the view behavior.
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class CarritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrito
        fields = ['nombre','precio','rutaI']

ViewSets define the view behavior.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = catalogo
        fields = ['nombre','precio','imagen','tipo']

ViewSets define the view behavior.
class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = catalogo.objects.all()
    serializer_class = CatalogoSerializer

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['NombreC','telefono','direccion','fecha']

ViewSets define the view behavior.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

router = routers.DefaultRouter()
router.register(r'Tipo', TipoViewSet)
router.register(r'Carrito', CarritoViewSet)
router.register(r'Catalogo', CatalogoViewSet)
#router.register(r'Pedido', PedidoViewSet)
urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('Decoraciones.urls', namespace='Decoraciones' )),
    path('Usuario/', include('Usuario.urls', namespace='usuario')),
    path('Usuario/', include('django.contrib.auth.urls')),
    path('accounts/login/',Login.as_view(), name="login"),
    path('logout/',login_required(logoutUsuario), name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Desarrollo de urls -> Usuario:
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,logout_then_login
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('descargar_pdf/', views.download_pdf, name='descargar_pdf'),
    path('Registro/', views.regist_U.as_view(),name = "regist_u"),
    path('Contrato/', views.Proforma, name="contrato"),
    path('Agregar/', views.agregar, name="carrito"),
    path('lista/', views.lista, name="bolsa"),
    path('Borrar/<int:numero>/', views.borrar, name='borrar'),
    path('Usuario/deshacer/<int:history_id>/', views.deshacer_cambio, name='deshacer_cambio')
    ]

Desarrollo de views -> Usuario:
...mucho codigo...

##  Plantillas Bootstrap
Se presenta la pagina de inicio, para ver el catalogo de productos
![Diagrama Entidad-Relación](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/Captura%20desde%202023-08-06%2019-40-35.png)
Login del usuario
![Diagrama Entidad-Relación](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/Captura%20desde%202023-08-06%2019-40-47.png)
Solamente se utilizo una plantilla para avizos de error durante, el login
![Diagrama Entidad-Relación](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/Captura%20desde%202023-08-06%2019-40-53.png)
##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de Proformas tiene valor de aceptación para los cliente finales (Personas Externas) radica en realizar el proceso de agregar al carrito propiamente, que empieza desde que:
    1. El Cliente inicia sesión, para tener acceso al carrito.
    2. El alumno selecciona el o los producto en la ventana Home.
    4. El alumno puede tener la posibilidad de quitar un producto por varias razones: cambio de producto, corregir error, etc.
    5. El alumno puede ver el total de su carrito, mediante la pestaña de su perfil.
    5. El alumno puede Descargar su contrato en forma de pdf.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
Video

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de productos de un catalogo, Tipos y Pedidos establecidos para que el administrador sea capaz de ver estas listas
    2. POST : Con este método se enviara el productos, tipos.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar descarga de un pdf, sobre el carrito que este posee
    Se muestran los pasos necesarios a realizar.
    video

##  Investigación: Email, Upload.
    No se logro
Github del proyecto:https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS
-   

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
