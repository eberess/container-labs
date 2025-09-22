from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    is_available = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    isbn = Column(String, unique=True, index=True) # Ajout du champ ISBN

    author = relationship("Author", back_populates="books")
    borrower = relationship("Member", back_populates="borrowed_books")

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    borrowed_books = relationship("Book", back_populates="borrower")