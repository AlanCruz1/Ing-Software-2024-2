import React from "react";
import "./RegistrarCliente.css"; // Importar estilos CSS

function RegistrarCliente() {
  return (
    <div>
      <h3>Registrar Cliente</h3>
      <form>
        <label htmlFor="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" />
        <label htmlFor="apellido">Apellido:</label>
        <input type="text" id="apellido" name="apellido" />
        <button className="registrar-btn">Registrar</button>
      </form>
    </div>
  );
}

export default RegistrarCliente;
