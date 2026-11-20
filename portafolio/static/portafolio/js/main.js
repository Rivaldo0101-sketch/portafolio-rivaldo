const botonTodos = document.getElementById("filtro-todos");
const botonWeb = document.getElementById("filtro-web");
const botonMovil = document.getElementById("filtro-movil");

const proyectos = document.querySelectorAll(".tarjeta-proyecto");

function filtrarProyectos(tipo) {
    proyectos.forEach(function(proyecto) {
        if (tipo === "todos" || proyecto.classList.contains(tipo)) {
            proyecto.style.display = "block";
        } else {
            proyecto.style.display = "none";
        }
    });
}

if (botonTodos) {
    botonTodos.addEventListener("click", function() {
        filtrarProyectos("todos");
    });

    botonWeb.addEventListener("click", function() {
        filtrarProyectos("web");
    });

    botonMovil.addEventListener("click", function() {
        filtrarProyectos("movil");
    });
}
const formulario = document.getElementById("formulario-contacto");

if (formulario) {
    formulario.addEventListener("submit", function(evento) {
        evento.preventDefault();

        const nombre = document.getElementById("nombre").value.trim();
        const correo = document.getElementById("correo");
        const mensaje = document.getElementById("mensaje").value.trim();
        const respuesta = document.getElementById("respuesta-formulario");

        if (nombre === "" || correo.value.trim() === "" || mensaje === "") {
            respuesta.textContent = "Completa todos los campos.";
            return;
        }

        if (!correo.checkValidity()) {
            respuesta.textContent = "Escribe un correo electrónico válido.";
            return;
        }

        respuesta.textContent =
            "Validación completada. Este formulario es una demostración " +
            "y no envía mensajes. Puedes contactarme por correo.";
    });
}
const botonMenu = document.getElementById("boton-menu");
const menu = document.getElementById("menu");

if (botonMenu && menu) {
    botonMenu.addEventListener("click", function() {
        menu.classList.toggle("abierto");

        const abierto = menu.classList.contains("abierto");
        botonMenu.setAttribute("aria-expanded", abierto);
    });
}