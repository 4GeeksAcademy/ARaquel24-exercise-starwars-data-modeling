import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date_inscription = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_people= Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
   
class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_planet= Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
   
class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)
  
    def to_dict(self):
        return {}
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
