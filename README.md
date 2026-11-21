# Portafolio de Rivaldo Tale

Proyecto del curso de Introducción a Programación Web.
Presenta mi formación, habilidades y proyectos académicos.

## Sitio publicado

https://portafolio-rivaldo.onrender.com/

## Tecnologías

- Python y Django.
- HTML.
- CSS.
- JavaScript.
- WhiteNoise para servir los archivos estáticos.
- Gunicorn para ejecutar la aplicación en Render.

## Páginas

- Inicio.
- Sobre mí.
- Habilidades.
- Proyectos.
- Contacto.
- Página de error 404.

## Funciones

- Menú desplegable para pantallas pequeñas.
- Filtros de proyectos: Todos, Web y Móvil.
- Validación de campos vacíos y formato del correo.
- Mensaje de confirmación al completar el formulario.
- Diseño adaptable a computadora y celular.

El formulario es una demostración: no envía mensajes.
El sitio no necesita guardar información en una base de datos.

## Cómo ejecutar el proyecto en Windows

Necesitas tener Python y Git instalados.

### 1. Descargar el proyecto

Abre una terminal y ejecuta estos comandos, uno después del otro:

```powershell
git clone https://github.com/Rivaldo0101-sketch/portafolio-rivaldo.git
cd portafolio-rivaldo
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Instalar Django y las dependencias

Este comando instala los paquetes incluidos en requirements.txt:

```powershell
.venv\Scripts\python -m pip install -r requirements.txt
```

### 4. Iniciar el servidor

Para trabajar localmente, comprueba que DEBUG esté activado en
mi_portafolio/settings.py. Si se configura automáticamente según el
entorno, conserva esa configuración.

Ejecuta:

```powershell
.venv\Scripts\python manage.py runserver
```

Abre esta dirección en el navegador:

http://127.0.0.1:8000/

Para detener el servidor, presiona Ctrl + C en la terminal.

## Cómo probar la página 404

Puedes verla directamente en el sitio publicado:

https://portafolio-rivaldo.onrender.com/no-existe/

Para probarla en tu computadora, cambia temporalmente estas opciones
en mi_portafolio/settings.py:

```python
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

Conserva las demás configuraciones del archivo y ejecuta:

```powershell
.venv\Scripts\python manage.py runserver --insecure
```

Abre:

http://127.0.0.1:8000/no-existe/

Aparecerá la página personalizada con el botón para volver al inicio.

Después de probarla, restaura la configuración anterior de DEBUG
y ALLOWED_HOSTS.

El argumento --insecure se utiliza únicamente para esta prueba local.

## Autor

Rivaldo Tale.

Técnico Universitario en Informática.
Universidad del Valle de Guatemala, Campus Altiplano.
