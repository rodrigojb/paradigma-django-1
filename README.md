## [Aprende Django. Capítulo 1.](https://www.youtube.com/watch?v=tqqeOtMidQU)

Django se basa en el patrón Modelo-Vista-Template (Apenas difiere con el patrón MVC)
Por defecto Django nos configura una base SQLite muy chica para las operaciones de DB.

Cuando aplicamos las migraciones por defecto podemos encontrar en la DB:
- Una tabla auth para la aplicacion nativa de Auth de Django, esta es una app de gestion de Usuarios, Grupos y Permisos.
- La tabla django_migrations que almacena las migrations aplicadas de las distintas apps.

Como funciona el modelo MVT?

- Un usuario accede a la app a traves de un URL Dispatcher (Nuestro archivo de urls).
- El archivo de urls se encarga de, en funcion de la url y los parametros, definir cual es la vista que tiene asociada.
Por ej: Para /home va esta vista.
- Que es una vista? El archivo views.py es donde se contiene la logica del endpoint, o la pagina que vayamos a mostrar.
Como buena práctica se pone toda la lógica en las vistas, no debemos dejar logica en los templates ni en los modelos para no acoplarnos mucho a ellos.
Desde las vistas podemos acceder a otras vistas o a otros 2 bloques, los modelos y los templates.
- Que son los modelos? Los modelos de BD
- Que son los templates? Son nuestra capa de renderizado, donde vamos a renderizar la info de las vistas, para mostrarlo al usuario.

Cual es la diferencia con el patrón MCV:
- EL controlador de MCV seria la vista en MVT.
- La vista de MCV seria el template en MVT.

Cada nueva aplicacion debemos darla de alta en el config de mi proyecto, dentro del archivo settings.py, en la seccion INSTALLED_APPS.

Los nombres que les definimos a las urls nos desacoplan de la url en sí, de la vista y del dispatcher, podemos usarlos para hacer referencia en los templates.
De esta forma, si cambiamos una url, no tenemos que cambiarla en cada lugar que se referencie, ya que lo accedemos a traves del nombre.

##### Comandos utiles:

```python
django-admin startproject <nombre> # Crea el proyecto de django con el nombre especificado.
python manage.py startapp <nombre> # Crea una aplicacion con el nombre especificado sobre el proyecto general.
python manage.py run server # Arranca el servidor de Django.
python manage.py migrate # Aplica las migraciones.
```

## [Aprende Django. Capítulo 2.](https://www.youtube.com/watch?v=BOS68i0KPeg)

#### Modelos
Las clases se representan como tablas (django.db.models.Model).
Los atributos se representan como columnas (django.db.models.Field).
Las instancias se representan como filas.

El metodo __str__ indica como debe representarse una instancia de esa clase. Sirve para ver el listado de instancias en el admin. Por ejemplo: Ladrón(Category.object(1))

#### Migraciones
- Se almacenan archivos con los cambios incrementales a nuestros modelos ya creados.
- Se almacenan en una tabla las migraciones ya aplicadas.

```python
python manage.py makemigrations # Crea el archivo con los cambios de bases de datos a ejecutar.
python manage.py migrate # Aplica los cambios a la base de datos.
```

#### Admin
Djando trae incoporado un panel de administración para tener una interfaz web sobre el contenido de la DB.

Para que nuestros modelos aparezcan en el panel de admin debemos darlos de alta en el archivo admin.py.

```python
python manage.py createsuperuser # Crea un usuario para ingresar al admin.
```
#### ModelViews - Vistas de clase
Django te provee de vistas ya pre-hechas para que le digas que modelo aplica. Esta funcionalidad sirve para listar asi como ver un elemento en concreto, crear uno nuevo, modificarlo, etc. Esto nos da facilidad para cada modelo, y asi no hacer la misma vista una y otra vez.

Nos proveen funciones predefinidas que podemos sobreescribir segun necesitemos. 
Por ejemplo: get_context_data()

Los hay de varios tipos: ListView, DetailView, CreateView, etc.

##### ListView
Otorga una vista que lista los objetos del modelo. Nos retorna una variable objectlist(nombre por defecto) que vamos a manipular en nuestro template, con el formato que le hayamos dado en nuestra ListView (queryset, ordering, etc).

##### DetailView
Su objetivo es el de detallar un objeto concreto de la DB. Ver en mayor detalle la info referida a una instancia del Modelo.

##### CreateView
Nos facilita la creación de una instancia
