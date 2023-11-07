# API de Gestión de Tareas con Django

## Descripción del Proyecto

Este proyecto es una API de gestión de tareas diseñada para permitir a los usuarios crear, actualizar, eliminar y visualizar tareas de forma eficiente. Utiliza Django y Django REST Framework para garantizar una arquitectura robusta y escalable, con autenticación JWT para la seguridad y Swagger combinado con Spectacular para la documentación de la API.

## Tecnologías Utilizadas

- **Django**: Framework de alto nivel para desarrollo web rápido y limpio.
- **Django REST Framework**: Un potente y flexible kit de herramientas para construir APIs Web.
- **Swagger**: Herramienta de interfaz para describir estructuras de APIs RESTful expresadas usando JSON.
- **JWT (JSON Web Tokens)**: Estándar abierto (RFC 7519) que define una forma compacta y autónoma para transmitir información de forma segura entre partes como un objeto JSON.
- **drf-spectacular**: Extensión de Django REST Framework que proporciona un esquema generación de esquemas OpenAPI con herramientas espectaculares.

## Características

- **Autenticación de Usuarios**: Seguridad mediante tokens JWT.
- **CRUD de Tareas**: Los usuarios pueden crear, leer, actualizar y eliminar tareas.
- **Documentación Interactiva**: Gracias a Swagger y drf-spectacular, los desarrolladores pueden probar fácilmente los endpoints de la API.
- **Filtrado y Ordenamiento**: Los usuarios pueden ordenar y filtrar las tareas según varios parámetros.

## Cómo Empezar

Para poner en marcha el proyecto en tu entorno local, sigue estos pasos:

1. Clona el repositorio:

```
https://github.com/JorgeRomeroC/tasks.git
cd tasks
```

2. Instala las dependencia:
```
pip install -r requirements.txt
```

3. Realiza las migraciones:
```
python manage.py migrate

```

3. Corre el servidor de desarrollo::
```
python manage.py runserver

```

## Si deseas tener acceso al panel de administracion Django

- EL proyecto guarda sus datos en una base de datos SQLite

1. Una vez levantado el proyecto con 
  ```
python manage.py runserver

```
2. Accede a la url
   

http://localhost:8000/admin

3. Ingresa las credenciales
   
user: cleverit
pass: 12345678

4. Para acceder a la documentación creada con Swagger

http://127.0.0.1:8000/api/schema/swagger/


## Para hacer uso de los endponits de la API

1. Deberas ir en la vista de la documentación Swagger en la sección TOKEN y ingresar las credenciales otorgadas arriba

<img width="1471" alt="Captura de pantalla 2023-11-07 a la(s) 03 28 30" src="https://github.com/JorgeRomeroC/tasks/assets/33013656/742b37a8-70cd-4856-81fc-42ced7656eb4">

2. Copia el token de acceso como se ve en la imagen

![Captura de pantalla 2023-11-07 a la(s) 03 33 57](https://github.com/JorgeRomeroC/tasks/assets/33013656/00b16dcc-424a-4191-b358-a19a5274eb20)

3. Ve a la zona superior, en el boton Authorize, y en el recuadro que te aparezca ingresa el token que copiaste
   
![Captura de pantalla 2023-11-07 a la(s) 03 36 25](https://github.com/JorgeRomeroC/tasks/assets/33013656/7761990d-f21b-4852-8c6f-3cb3d82b9178)

## Ahora podras hacer uso de las acciones CRUD de esta API TASKS


