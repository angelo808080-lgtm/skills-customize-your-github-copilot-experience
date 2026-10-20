"""
Building REST APIs with FastAPI - Starter Code

Setup:
    pip install fastapi uvicorn

Run (after saving this file as main.py):
    uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs to try your endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")

# In-memory "database" of books
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 2, "title": "Automate the Boring Stuff with Python", "author": "Al Sweigart"},
    {"id": 3, "title": "Think Python", "author": "Allen B. Downey"},
]


# TODO (Task 3): Define a Book model with title and author fields
class Book(BaseModel):
    pass


# TODO (Task 1): Return a welcome message
@app.get("/")
def read_root():
    pass


# TODO (Task 2): Return the full list of books
@app.get("/books")
def get_books():
    pass


# TODO (Task 2): Return a single book, or raise HTTPException(status_code=404) if not found
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


# TODO (Task 3): Add a new book with a unique id and return it
@app.post("/books")
def create_book(book: Book):
    pass
