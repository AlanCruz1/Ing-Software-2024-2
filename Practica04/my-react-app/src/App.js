import React, { useState } from "react";
import Cliente from "./components/Clientes/Clientes";
import Peliculas from "./components/Peliculas/Peliculas";
import Rentas from "./components/Rentas/Rentas";

function App() {
  const [opcionSeleccionada, setOpcionSeleccionada] = useState("Cliente");

  const mostrarContenido = () => {
    switch (opcionSeleccionada) {
      case "Cliente":
        return <Cliente />;
      case "Peliculas":
        return <Peliculas />;
      case "Rentas":
        return <Rentas />;
      default:
        return null;
    }
  };

  return (
    <div>
      <h1>Menú</h1>
      <ul>
        <li onClick={() => setOpcionSeleccionada("Cliente")}>Cliente</li>
        <li onClick={() => setOpcionSeleccionada("Peliculas")}>Peliculas</li>
        <li onClick={() => setOpcionSeleccionada("Rentas")}>Rentas</li>
      </ul>
      {mostrarContenido()}
    </div>
  );
}

export default App;
