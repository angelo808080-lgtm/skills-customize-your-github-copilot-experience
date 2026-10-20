# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API in Python using the FastAPI framework, creating endpoints that read, create, and update data using HTTP methods.

## 📝 Tasks

### 🛠️ Create Your First Endpoint

#### Description
Set up a FastAPI application using the provided starter code and create a root endpoint that returns a welcome message. Run the server with `uvicorn` and test it in your browser.

#### Requirements
Completed program should:

- Create a `FastAPI` app instance
- Respond to `GET /` with a JSON message such as `{"message": "Welcome to the Book API"}`
- Save the starter code as `main.py` and run it locally with `uvicorn main:app --reload`

### 🛠️ Read Data with GET Endpoints

#### Description
Use the in-memory list of books in the starter code to build endpoints that return all books and a single book by its ID.

#### Requirements
Completed program should:

- Respond to `GET /books` with the full list of books
- Respond to `GET /books/{book_id}` with the matching book
- Return a `404` error with a helpful message when the book does not exist

```
GET /books/1
{"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"}
```

### 🛠️ Add Data with a POST Endpoint

#### Description
Define a Pydantic model for a book and create an endpoint that lets users add a new book to the list.

#### Requirements
Completed program should:

- Define a `Book` model with `title` and `author` fields
- Respond to `POST /books` by adding the book with a new unique ID
- Return the newly created book in the response
- Be testable through the automatic docs at `/docs`
