import React from 'react';
import { Link, Route, Switch } from 'react-router-dom';
import ListarRentas from './ListarRentas';
import ActualizarRentas from './ActualizarRentas';
import './Rentas.css'; // Importar estilos CSS

function Rentas() {
  return (
    <div className="rentas-container">
      <h2>Menú de Rentas</h2>
      <nav className="rentas-menu">
        <ul>
          <li>
            <Link to="/rentas/listar">Listar Rentas</Link>
          </li>
          <li>
            <Link to="/rentas/actualizar">Actualizar Rentas</Link>
          </li>
        </ul>
      </nav>
      <Switch>
        <Route path="/rentas/listar" component={ListarRentas} />
        <Route path="/rentas/actualizar" component={ActualizarRentas} />
      </Switch>
    </div>
  );
}

export default Rentas;
