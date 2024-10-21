from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base that holds table objects
Base = declarative_base()

# creating db relationships

class passmanUser(Base):
    __tablename__ = 'passman_user'
    