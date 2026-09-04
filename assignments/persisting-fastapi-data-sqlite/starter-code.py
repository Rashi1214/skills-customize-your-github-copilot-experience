"""Starter code for the Persisting FastAPI Data with SQLite assignment."""

import sqlite3

from fastapi import FastAPI

app = FastAPI(title="Persistent Book API")
DATABASE = "books.db"


def get_connection():
    """Open a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create the books table if it does not exist."""
    connection = get_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


initialize_database()


@app.get("/")
def read_root():
    """Return a welcome message from the API root."""
    return {"message": "Welcome to the Persistent Book API"}


# TODO: Define a Pydantic model for book requests.
# TODO: Add GET /books to read all books from SQLite.
# TODO: Add GET /books/{book_id} to read one book or return a 404 error.
# TODO: Add POST /books to insert a book and return status code 201.
# TODO: Add PUT /books/{book_id} to update an existing book.
# TODO: Add DELETE /books/{book_id} to delete an existing book.
# TODO: Close every database connection after its operation.
# TODO: Run the API with: uvicorn starter-code:app --reload
