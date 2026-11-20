# Portafolio de Rivaldo Tale

Proyecto del curso de Introducción a Programación Web.
Presenta mi formación, habilidades y proyectos académicos.

## Tecnologías

- Python y Django.
- HTML.
- CSS.
- JavaScript.

## Páginas

- Inicio.
- Sobre mí.
- Habilidades.
- Proyectos.
- Contacto.
- Página de error 404.

## Funciones

- Menú para pantallas pequeñas.
- Filtros de proyectos: Todos, Web y Móvil.
- Validación de campos vacíos y formato del correo.
- Mensaje de confirmación al completar el formulario.
- Diseño adaptable a computadora y celular.

El formulario es una demostración: no envía mensajes.
El sitio no necesita guardar información en una base de datos.

## Cómo ejecutar el proyecto en Windows

Necesitas tener Python y Git instalados.

### 1. Descargar el proyecto

Abre una terminal y ejecuta:

```powershell
git clone https://github.com/Rivaldo0101-sketch/portafolio-rivaldo.git
cd portafolio-rivaldo
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Instalar Django

```powershell
.venv\Scripts\python -m pip install django
```

### 4. Iniciar el servidor

Comprueba que en mi_portafolio/settings.py esté DEBUG = True.

```powershell
.venv\Scripts\python manage.py runserver
```

Abre esta dirección en el navegador:

http://127.0.0.1:8000/

Para detener el servidor, presiona Ctrl + C en la terminal.

## Cómo probar la página 404

En mi_portafolio/settings.py, cambia temporalmente:

```python
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

Inicia el servidor con este comando para cargar también los estilos durante la prueba local:

```powershell
.venv\Scripts\python manage.py runserver --insecure
```

Abre:

http://127.0.0.1:8000/no-existe/

Aparecerá la página personalizada con el botón para volver al inicio.

Después de probarla, vuelve a poner DEBUG = True.
El comando con --insecure se utiliza solamente para esta prueba local.

## Autor

Rivaldo Tale.

Técnico Universitario en Informática.
Universidad del Valle de Guatemala, Campus Altiplano. 