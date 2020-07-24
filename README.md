
[Aprende Django. Capítulo 1.](https://www.youtube.com/watch?v=tqqeOtMidQU)

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

Comandos utiles:

django-admin startproject <nombre> - Crea el proyecto de django con el nombre especificado
python manage.py startapp <nombre> - Crea una aplicacion con el nombre especificado sobre el proyecto general
python manage.py run server - Arranca el servidor de Django
python manage.py migrate - Aplica las migraciones