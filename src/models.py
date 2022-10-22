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

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    passenger = Column(String(250))
    cost_in_credits = Column(String(250))
    vehicle_class = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')