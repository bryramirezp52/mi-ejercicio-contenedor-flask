# Minimal Clicker Flask

Un juego clicker minimalista implementado en un solo archivo con Flask, **ahora completamente contenedorizado con Docker**. Este proyecto está diseñado para demostrar la implementación de una aplicación web básica y su despliegue mediante contenedores.

---

## Descripción

Esta aplicación web cuenta las veces que se hace clic en un círculo grande y blanco sobre un fondo naranja. El contador se guarda en memoria del servidor y se reinicia con cada proceso (lo cual es una simplificación para este ejemplo). El objetivo principal de este repositorio es ilustrar:

* **Fundamentos de Flask**: Manejo de rutas y lógica de backend.
* **Interacciones Frontend-Backend**: Realización de peticiones AJAX desde el navegador para actualizar la interfaz sin recargar la página.
* **Contenerización con Docker**: Empaquetar una aplicación Python/Flask dentro de un contenedor Docker para asegurar un entorno de ejecución **consistente, reproducible y portable**.

---

## Cómo usar

Asegúrate de tener **Docker instalado y en ejecución** en tu sistema.

1.  **Clona este repositorio:**
    ```bash
    git clone https://github.com/bryramirezp52/mi-ejercicio-contenedor-flask.git
    cd mi-ejercicio-contenedor-flask
    ```

2.  **Construye la imagen Docker:**
    ```bash
    docker build -t minimal-clicker .
    ```
    *Este comando lee el `Dockerfile` y crea una imagen de Docker llamada `minimal-clicker`. El archivo `.dockerignore` asegura que solo los archivos necesarios sean copiados a la imagen, optimizando su tamaño.*

3.  **Ejecuta el contenedor Docker:**
    ```bash
    docker run -p 5000:5000 --name clicker-app minimal-clicker
    ```
    *Esto inicia un contenedor a partir de tu imagen, mapeando el puerto 5000 del contenedor al puerto 5000 de tu máquina local. Se le asigna el nombre `clicker-app` para facilitar su gestión.*

4.  Abre tu navegador web y ve a `http://localhost:5000`.

5.  Haz clic en el círculo para incrementar el contador.

---

## Estructura del Proyecto

* **`Dockerfile`**: Contiene las instrucciones para construir la imagen Docker de la aplicación.
* **`.dockerignore`**: Especifica los archivos y directorios que Docker debe ignorar al construir la imagen, como entornos virtuales o archivos de caché.
* **`app.py`**: El código principal de la aplicación Flask, que incluye el HTML, CSS y JavaScript embebidos.
* **`requirements.txt`**: Lista todas las dependencias de Python que la aplicación necesita para funcionar.
* **`README.md`**: Este archivo de descripción del proyecto y sus instrucciones.

---

## Notas Importantes

* **Persistencia del Contador**: El contador se almacena en una variable global en memoria dentro del contenedor. Esto significa que si el contenedor se detiene, se reinicia o se elimina, el contador volverá a cero. Para una persistencia real en una aplicación de producción, sería necesario integrar una base de datos externa o utilizar volúmenes persistentes de Docker.
* **Modo Desarrollo**: La aplicación Flask se ejecuta en modo desarrollo (`debug=True`). Esto es útil para la depuración y el desarrollo rápido, pero **no es adecuado para entornos de producción**. En un despliegue real, se utilizaría un servidor WSGI (como Gunicorn o uWSGI) para servir la aplicación de manera más robusta y segura.

---

## Limpieza de Recursos Docker

Una vez que hayas terminado de usar la aplicación, puedes limpiar los recursos de Docker para liberar espacio:

1.  **Detener el contenedor en ejecución:**
    ```bash
    docker stop clicker-app
    ```

2.  **Eliminar el contenedor:**
    ```bash
    docker rm clicker-app
    ```

3.  **Eliminar la imagen Docker (opcional, si no la vas a usar más):**
    ```bash
    docker rmi minimal-clicker
    ```
    *Asegúrate de que no haya ningún contenedor usando esta imagen antes de intentar eliminarla.*

---

## Tecnologías Usadas

* **Python 3**
* **Flask** (microframework web para Python)
* **HTML5, CSS3 y JavaScript** (con la Fetch API para interacciones asíncronas)
* **Docker** (para la contenedorización y gestión del entorno)
