import React from "react";
import "./EliminarPelicula.css"; // Importar estilos CSS

function EliminarPelicula() {
  return (
    <div className="eliminar-pelicula-container">
      <h3>Eliminar Película</h3>
      <form>
        <label htmlFor="titulo">Título:</label>
        <input type="text" id="titulo" name="titulo" />
        <button className="eliminar-btn">Eliminar</button>
      </form>
    </div>
  );
}

export default EliminarPelicula;
