# Minimal Clicker Flask

Un juego clicker minimalista implementado en un solo archivo con Flask.

---

## Descripción

Esta aplicación web cuenta las veces que se hace clic en un círculo grande y blanco sobre un fondo naranja. El contador se guarda en memoria del servidor y se reinicia cada vez que el proceso se reinicia.

Ideal para aprender a manejar rutas en Flask y hacer peticiones AJAX desde el navegador para actualizar la interfaz sin recargar la página.

---

## Cómo usar

1.  Asegúrate de tener Python 3 instalado.
2.  Instala Flask si aún no lo tienes:

    ```bash
    pip install flask
    ```

3.  Ejecuta la app:

    ```bash
    python app.py
    ```

4.  Abre tu navegador y ve a `http://localhost:5000`.

5.  Haz clic en el círculo para incrementar el contador.

---

## Estructura

* **`app.py`**: Código completo de la aplicación, incluye frontend (HTML, CSS, JS) embebido y backend en Flask.

---

## Notas

* El contador se almacena en una variable global en memoria, por lo que si reinicias el servidor se reseteará a cero.
* El servidor corre en modo desarrollo con `debug=True` para facilitar pruebas y desarrollo.

---

## Tecnologías usadas

* Python 3
* Flask
* HTML5, CSS3 y JavaScript (fetch API)
