from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class peliculas(db.Model):
    __tablename__ ='peliculas'
    idPelicula = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(200),nullable = False)
    genero = Column(String(45),nullable = True)
    inventario = Column(Integer,nullable = False)

    def __init__(self, nombre, genero=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.inventario = inventario

    def __str__(self):
        return f'Nombre: {self.nombre}\nGenero: {self.genero}'
               