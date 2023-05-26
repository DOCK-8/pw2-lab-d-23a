const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// Ruta principal
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Ruta para ver todos los eventos
app.get('/eventos', (req, res) => {
  fs.readdir('./eventos', (err, files) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error al leer los eventos');
    } else {
      const eventos = files.map((file) => file.split('.')[0]);
      res.send(eventos);
    }
  });
});

// Ruta para ver los detalles de un evento
app.get('/eventos/:evento', (req, res) => {
  const evento = req.params.evento;
  fs.readFile(`./eventos/${evento}.txt`, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.status(404).send('Evento no encontrado');
    } else {
      res.send(data);
    }
  });
});

// Ruta para crear un evento
app.post('/eventos', (req, res) => {
  const titulo = req.body.titulo;
  const descripcion = req.body.descripcion;

  fs.access(`./eventos/${titulo}.txt`, fs.constants.F_OK, (err) => {
    if (!err) {
      res.status(409).send('El evento ya existe');
    } else {
      const eventoData = `${titulo}\n${descripcion}`;

      fs.writeFile(`./eventos/${titulo}.txt`, eventoData, 'utf8', (err) => {
        if (err) {
          console.error(err);
          res.status(500).send('Error al crear el evento');
        } else {
          res.redirect('/');
        }
      });
    }
  });
});

// Ruta para eliminar un evento
app.delete('/eventos/:evento', (req, res) => {
  const evento = req.params.evento;
  fs.unlink(`./eventos/${evento}.txt`, (err) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error al eliminar el evento');
    } else {
      res.send('Evento eliminado exitosamente');
    }
  });
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`La aplicaci�n est� escuchando en el puerto ${port}`);
});

