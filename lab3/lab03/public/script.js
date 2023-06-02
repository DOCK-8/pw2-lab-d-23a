  document.addEventListener('DOMContentLoaded', () => {
  const crearEventoForm = document.getElementById('crearEventoForm');
  const eventosList = document.getElementById('eventosList');

  // Cargar eventos al iniciar
  cargarEventos();

  // Enviar formulario para crear evento
  crearEventoForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const titulo = document.getElementById('titulo').value;
    const descripcion = document.getElementById('descripcion').value;
    crearEvento(titulo, descripcion);
  });

  // Cargar eventos
  function cargarEventos() {
    fetch('/eventos')
      .then((response) => response.json())
      .then((data) => {
        eventosList.innerHTML = '';
        data.forEach((evento) => {
          const li = document.createElement('li');
          li.innerText = evento;
          eventosList.appendChild(li);
        });
      })
      .catch((error) => console.error(error));
  }

  // Crear evento
  function crearEvento(titulo, descripcion) {
    fetch('/eventos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `titulo=${encodeURIComponent(titulo)}&descripcion=${encodeURIComponent(descripcion)}`,
    })
      .then((response) => {
        if (response.ok) {
          cargarEventos();
          crearEventoForm.reset();
        } else {
          throw new Error(response.statusText);
        }
      })
      .catch((error) => console.error(error));
  }
});

