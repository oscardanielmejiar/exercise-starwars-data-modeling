import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

#python src/models.py to create
# a new diagram showing changes

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    user_id = Column(ForeignKey('Favorites.id'))

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    person_name = Column(String(250), unique=True)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    planets_id = Column(ForeignKey('Planets.id'))
    vehicles_id = Column(ForeignKey('Vehicles.id'))

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250),unique=True)
    diameter = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(String(250))
    person_id = Column(Integer, ForeignKey('Person.id'))


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    passenger = Column(String(250))
    cost_in_credits = Column(String(250))
    vehicle_class = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    favorite_name = Column(String(250), nullable=False)
    user_id = Column(ForeignKey('User.id'))
    person_id = Column(ForeignKey('Person.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
