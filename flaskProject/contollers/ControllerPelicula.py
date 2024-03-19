from flask import Blueprint, request, render_template, flash, url_for, redirect
from model import model_peliculas as modeloPelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/buscarPelicula', methods=['GET', 'POST'])
def mostrar_pelicula_por_id():
     if request.method == "GET":
        return render_template('leer_peliculas.html')
     else:

        id = request.form["peliculaId"]
        pelicula = modeloPelicula.leer_pelicula_por_id(id)
        if pelicula is not None:
           return render_template("mostrar_pelicula.html", pelicula=pelicula)
        else:
            return render_template("mensaje.html", mensaje= "No existe pelicula con dicho Id")
     
@pelicula_blueprint.route('/borrar', methods=['GET', 'POST'])
def eliminar_pelicula_por_id():
     if request.method == "GET":
        return render_template('borrar_peliculas.html')
     else:

        id = request.form["peliculaId"]
        print(id)
        retorno = modeloPelicula.eliminar_pelicula(id)
         
        if retorno == -1:
            return render_template("mensaje.html", mensaje="Ha habido un error al intentar borrar")
        else:
            return render_template("mensaje.html", mensaje="Película borrada con éxito")


@pelicula_blueprint.route('/registro', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == "GET":
        return render_template('crear_pelicula.html')
    else:

        nombre = request.form["nombre"]
        print(nombre)
        genero = request.form["genero" ]
        print(genero)
        inventario = request.form["inventario"]
        print(inventario)

        if duracion == '':
            duracion = None
            print("detectado")
        else:
            duracion = int(duracion)
            print("No detectado")

        if inventario == '':
            inventario = 1
            print("detectado")
        else:
            inventario = int(inventario)
            print("No detectado")
   

        retorno = modeloPelicula.crear_pelicula(nombre, genero, duracion, inventario)
       
            
        
       
        
        if retorno == -1:
            return render_template("mensaje.html", mensaje="Ha habido un error al crear esa película")
        else:
            return render_template("mensaje.html", mensaje="Pelicula creada con éxito")
    
    
    
@pelicula_blueprint.route('/leerPeliculas')
def mostrar_pelicula():
    peliculas = modeloPelicula.leer_peliculas()
    return render_template("mostrar_peliculas.html", peliculas=peliculas)

@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == "GET":
        return render_template('actualizar_pelicula.html')
    else:
        id = request.form["peliculaId"]
        print(id)
        nombre = request.form["nombre"]
        print(nombre)
        genero = request.form["genero" ]
        print(genero)
        duracion = request.form["duracion"]
        print(duracion)
        inventario = request.form["inventario"]
        print(inventario)
        
      
              
        retorno = modeloPelicula.actualizar_pelicula(id, nombre, genero, duracion, inventario)
        
        if retorno == -1:
            return render_template("mensaje.html", mensaje="Ha habido un error al querer actualizar")
        else:
            return render_template("mensaje.html", mensaje="Película actualizada con éxito")