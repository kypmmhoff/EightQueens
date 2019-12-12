import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Board(Base):
    __tablename__ = 'board'
    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)
    description = Column(String(24))

class Solution(Base):
    __tablename__ = 'solution'
    id = Column(Integer, primary_key=True)
    positions = Column(String(250), nullable=False)
    board_id = Column(Integer, ForeignKey('board.id'))
    board = relationship(Board)

# Engine = create_engine('sqlite:///sqlalchemy_example.db')    
# Engine = create_engine('postgres://postgres@db/postgres') 
conString = os.environ['CON_STRING'] 
Engine = create_engine(conString) 
Base.metadata.create_all(Engine)





