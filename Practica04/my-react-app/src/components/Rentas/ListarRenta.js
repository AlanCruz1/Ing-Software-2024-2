import React from "react";
import "./ListarRentas.css"; // Importar estilos CSS

function ListarRentas() {
  // Supongamos que tienes un arreglo de películas rentadas
  const peliculasRentadas = [
    { id: 1, titulo: "Pelicula 1", director: "Director 1" },
    { id: 2, titulo: "Pelicula 2", director: "Director 2" },
    { id: 3, titulo: "Pelicula 3", director: "Director 3" },
  ];

  return (
    <div className="listar-rentas-container">
      <h3>Listar Rentas</h3>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Director</th>
          </tr>
        </thead>
        <tbody>
          {peliculasRentadas.map((pelicula) => (
            <tr key={pelicula.id}>
              <td>{pelicula.id}</td>
              <td>{pelicula.titulo}</td>
              <td>{pelicula.director}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ListarRentas;
