from sqlalchemy import Column, Integer, String, LargeBinary, Boolean

from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    id_Usuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200), nullable=True)
    contrasena = Column(String(64))
    email = Column(String(500), nullable=True, unique=True)
    fotoPerfil = Column(LargeBinary, nullable=True)
    superUser = Column(Boolean, nullable=True)
    

    def __init__(self, nombre, ap_pat, contrasena, ap_mat=None,
                 email=None, foto_perfil=None, super_user=None):
        self.nombre = nombre
        self.apPat = ap_pat
        self.apMat = ap_mat
        self.contrasena = contrasena
        self.email = email
        self.fotoPerfil = foto_perfil
        self.superUser = super_user

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido paterno: {self.apPat}\nApellido materno: {self.apMat}\nEmail: {self.email}'