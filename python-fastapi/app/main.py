from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import get_db, Base, engine

# La base de données et les tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestion de Bibliothèque",
    description="Une API REST pour gérer les livres, les auteurs et les membres."
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion de bibliothèque !"}

# -----------------------------------------------------------------
# Section pour les auteurs
# -----------------------------------------------------------------

@app.post("/authors/", status_code=status.HTTP_201_CREATED, response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return authors

# -----------------------------------------------------------------
# Section pour les livres
# -----------------------------------------------------------------

@app.post("/books/", status_code=status.HTTP_201_CREATED, response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

# Nouvelle route pour récupérer un livre par son ISBN
@app.get("/books/isbn/{isbn}", response_model=schemas.Book)
def get_book_by_isbn(isbn: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    return book

# Nouvelle route pour emprunter un livre par son ISBN
@app.post("/books/borrow/{isbn}", response_model=schemas.Book)
def borrow_book(isbn: str, member_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    member = db.query(models.Member).filter(models.Member.id == member_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    if not member:
        raise HTTPException(status_code=404, detail="Membre non trouvé")
    if not book.is_available:
        raise HTTPException(status_code=400, detail="Livre déjà emprunté")
    
    book.is_available = False
    book.borrower = member
    db.commit()
    db.refresh(book)
    return book

# Nouvelle route pour rendre un livre par son ISBN
@app.post("/books/return/{isbn}", response_model=schemas.Book)
def return_book(isbn: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    if book.is_available:
        raise HTTPException(status_code=400, detail="Ce livre n'a pas été emprunté")
        
    book.is_available = True
    book.borrower = None
    db.commit()
    db.refresh(book)
    return book
# -----------------------------------------------------------------
# Routes pour les membres
# -----------------------------------------------------------------

@app.post("/members/", status_code=status.HTTP_201_CREATED, response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

@app.get("/members/", response_model=List[schemas.Member])
def read_members(db: Session = Depends(get_db)):
    members = db.query(models.Member).all()
    return members