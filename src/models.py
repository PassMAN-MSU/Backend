import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base that holds table objects
Base = declarative_base()

# 
# creating db relationships

class passmanUser(Base):
    __tablename__ = 'user'
               # data type,                   # lambda function so each uuid (str w/ len 36) is unique
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    password_list_id = Column(String(10), ForeignKey=True)
    username = Column(String(10), nullable=False, unique=True)

class passManPassword(Base):
    __tablename__ = 'password'
