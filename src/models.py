import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key = True)
    favorite = relationship("Favorite", back_populates="user")
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(20), nullable = False)
    date_sub = Column(Date, nullable = False)
    name =  Column(String(50), nullable = False)
    Last_Name = Column(String(50), nullable = True)

class Favorite(Base):
    __tablename__= "favorite"
    id = Column(Integer, primary_key = True)
    user = relationship("User", back_populates="favorite")
    user_id = Column(Integer, ForeignKey("user.id"))
    planet = relationship("planet")
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character = relationship("character")
    character_id = Column(Integer, ForeignKey("character"))
    vehicle = relationship("vehicle")
    vehicle_id = Column(Integer, ForeignKey("vehicle"))
    film = relationship("film")
    film_id = Column(Integer, ForeignKey("film"))

class Planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    gravity = Column(String(20))

class Character(Base):
    __tablename__= "character"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    hair_colorr = Column(String(20))
    eyes_color = Column(String(20))
    gender = Column(String(20))
    birthday = Column(Date)

class Vehicle(Base):
    __tablename__="vehicle"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    model = Column(String(20))
    max_speed = Column(Float)

class Film(Base):
    __tablename__="film"
    id = Column(Integer, primary_key = True)
    title = Column(String(20))
    lenght = Column(Integer)
    cast = Column(String)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')