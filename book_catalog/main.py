from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Book, Base
from schemas import BookBase, BookCreate, BookInDB, BookUpdate
from db import engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Endpoint to create a new book
@app.post("/books/", response_model=BookInDB)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Endpoint to retrieve a book by ID
@app.get("/books/{book_id}", response_model=BookInDB)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Endpoint to retrieve all books
@app.get("/books/", response_model=List[BookInDB])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Endpoint to update a book by ID
@app.put("/books/{book_id}", response_model=BookInDB)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for field, value in book.dict().items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

# Endpoint to delete a book by ID
@app.delete("/books/{book_id}", response_model=BookInDB)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book
