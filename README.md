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

##  Diagrama Entidad-Relación
    ![Diagrama]([url_de_la_imagen](https://github.com/WillianAyamamani/pw2-lab-d-23a/blob/main/lab7/PWEB/erd.png))

##  Administración con Django
    Se muestran los pasos realizados para crear el Proyecto, la aplicación, creacion de modelos, migraciones y habilitación del panel de administración en Django.
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: ...

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....

##  Investigación: Email, Upload.
    - Email: Se utilizará la funcionalidad del uso de envío de correos electrónicos cuando el proceso de inscripciones culmine y al profesor le llegue la lista de alumnos inscritos en sus grupos a cargo.
    - Upload: Se utilizará esta funcionalidad para subír, archivos CSV para importar y exportar información en el sistema.
    Se muestran los pasos realizados para su funcionamiento correcto.
    ...

Github del proyecto:

URL en Heroku:

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
