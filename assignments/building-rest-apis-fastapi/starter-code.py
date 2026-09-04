"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.get("/")
def read_root():
    """Return a welcome message from the API root."""
    return {"message": "Welcome to the Book API"}


# TODO: Define a Pydantic model for a book request.
# TODO: Add GET /books to return all books.
# TODO: Add GET /books/{book_id} to return one book or a 404 error.
# TODO: Add POST /books to validate and add a new book.
# TODO: Run the API with: uvicorn starter-code:app --reload
