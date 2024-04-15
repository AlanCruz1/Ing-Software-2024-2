import React from "react";
import AgregarPelicula from "./AgregarPelicula";
import EliminarPelicula from "./EliminarPelicula";
import "./Peliculas.css"; // Importar estilos CSS

function Pelicula() {
  return (
    <div className="pelicula-container">
      <h2>Menú de Películas</h2>
      <div className="menu">
        <AgregarPelicula />
        <EliminarPelicula />
      </div>
    </div>
  );
}

export default Pelicula;
