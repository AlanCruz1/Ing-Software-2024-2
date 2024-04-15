import React from "react";
import RegistrarCliente from "./RegistrarCliente";
import EliminarCliente from "./EliminarCliente";
import VerCliente from "./VerCliente";
import ActualizarCliente from "./ActualizarCliente";

function Cliente() {
  return (
    <div>
      <h2>Menú de Cliente</h2>
      <div>
        <RegistrarCliente />
        <EliminarCliente />
        <VerCliente />
        <ActualizarCliente />
      </div>
    </div>
  );
}

export default Cliente;
