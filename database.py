from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, create_engine

# Init the sqlalchemy engine
engine = create_engine("postgres://steffo:HIDDENPASSWORD@royal.steffo.eu:5432/pizzadev")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

# Create a new default session
session = Session()
