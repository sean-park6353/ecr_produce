
from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10), nullable= False)
    contents = Column(Text(300), default="", nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

class User(Base):
    
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), nullable=False)
    email = Column(String(30), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

class BookToUser(Base):
    
    __tablename__ = "book_user"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    

