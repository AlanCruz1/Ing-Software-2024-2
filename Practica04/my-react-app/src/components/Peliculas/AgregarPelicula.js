import React from "react";
import "./AgregarPelicula.css"; // Importar estilos CSS

function AgregarPelicula() {
  return (
    <div className="agregar-pelicula-container">
      <h3>Agregar Película</h3>
      <form>
        <label htmlFor="titulo">Título:</label>
        <input type="text" id="titulo" name="titulo" />
        <label htmlFor="director">Director:</label>
        <input type="text" id="director" name="director" />
        <button className="agregar-btn">Agregar</button>
      </form>
    </div>
  );
}

export default AgregarPelicula;
