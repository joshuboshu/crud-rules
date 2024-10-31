
# Aplicación web basica

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![HTML](https://img.shields.io/badge/HTML-orange?style=for-the-badge&logo=html5&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-blue?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/JavaScript)

Pagina web de gestión de un inventario de productos hecha utilizando [Python](https://python.org), [Django](https://www.djangoproject.com/), [bootstrap](https://getbootstrap.com/) y [Postgresql](https://www.postgresql.org/). La aplicación permite listar, agregar y eliminar productos, agregarles una descripción y marcar como disponibles o no disponibles, ademas se puede agregar mas de una caracteristicas a los productos.

## Tecnologías Utilizadas

- **Backend**: Django 5.1
- **Frontend(Templates)**: HTML, CSS, JavaScript
- **Base de Datos**: PostgreSQL 
- **Otros**: Bootstrap 5

## Requisitos
Es fundamental contar con estos requisitos para poder correr el proyecto:
- Docker
- Docker Compose

## Instrucciones para Ejecutar el Proyecto

1. Ingresa al repositorio:
   ```
   cd docker_project
    ```
2. Ejecuta los comandos en una terminal
    ```
    docker-compose build 
    ```
3. Realiza las migraciones correspondientes
    ```
    docker-compose run web python manage.py migrate
    ```
4. Puedes crear un super usuario (Opcional), en caso de que quieras manipular los datos desde el admin de Django
    ```
    docker-compose run web python manage.py createsuperuser
    ```
6. Finalmente, correremos el proyecto en el puerto 8000
    ```
    docker-compose up 
    ```
6. Accede al localhost

    ```
    http://127.0.0.1:8000/
    ```

7. En caso de tener problemas de permisos, ejecuta los siguientes comandos y luego vuelve a ejecutar los anteriores

    ```
    sudo usermod -aG docker $USER
    ```
    ```
    exec su -l $USER
    ```
    

## Una vez aquí se pueden realizar todas las acciones que permite la aplicación

### Lista de productos, podemos agregar mas productos, o bien, ver los detalles o eliminar productos
![](./images/lista.png)

### Podemos agregar un nuevo producto con una descripción y marcar como disponible, o bien, volver al inicio
![](./images/agregar.png)

### Detalles del producto, podemos agregar caracteristicas y editarlas, en el inicio saldra la descripción a menos que le agreguemos caracteristicas al producto.
![](./images/detalles.png)

### Podemos agregar una caracteristica, esta incluye un titulo y un valor, por ejempo **Pantalla:** IPS, podemos agregar varias caracteristicas
![](./images/agregar-detalle.png)

### Podemos editar las caracteristicas de los productos.
![](./images/editar-detalle.png)

## La aplicación tiene alertas por cada vez que se desee agregar un nuevo producto, eliminar un producto o eliminar una caracteristica.

### Eliminar producto.
![](./images/captura1.png)

### Agregar producto.
![](./images/captura2.png)

### Eliminar caracteristica.
![](./images/captura3.png)
