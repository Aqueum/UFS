#!/usr/bin/python3
# Configuration

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Class definitions


class Shelter(Base):

    # Table information
    __tablename__ = 'shelter'

    # Mappers
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(String(10))
    website = Column(String(80))
    id = Column(Integer, primary_key=True)


class Puppy(Base):

    # Table information
    __tablename__ = 'puppy'

    # Mappers
    name = Column(String(80), nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String(7))
    weight = Column(Numeric)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    picture = Column(String(80))

# End of file
engine = create_engine(
    'sqlite:///puppies.db'
)
Base.metadata.create_all(engine)
