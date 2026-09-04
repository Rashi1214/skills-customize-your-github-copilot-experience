# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend a FastAPI book API so that its data is stored in a SQLite database instead of an in-memory list. You will practice database connections, SQL queries, CRUD routes, validation, and persistent application state.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description

Use the provided starter code to create a SQLite database and a `books` table for the API.

#### Requirements

Completed program should:

- Connect to a SQLite database file named `books.db`.
- Create a `books` table when the application starts if it does not already exist.
- Store an integer `id`, a text `title`, and a text `author` for each book.
- Close database connections after each operation.

### 🛠️ Implement Persistent CRUD Routes

#### Description

Replace the in-memory book collection with SQL queries and add routes for creating, reading, updating, and deleting books.

#### Requirements

Completed program should:

- Return all stored books from `GET /books`.
- Return one book from `GET /books/{book_id}`.
- Insert a new book with `POST /books`.
- Update an existing book with `PUT /books/{book_id}`.
- Delete an existing book with `DELETE /books/{book_id}`.
- Preserve created books after the API is stopped and started again.

Example update request:

```json
{
  "title": "The Hobbit: An Unexpected Journey",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Handle Validation and Database Errors

#### Description

Make the API handle invalid input and missing records with clear JSON responses and appropriate HTTP status codes.

#### Requirements

Completed program should:

- Require non-empty `title` and `author` values for book requests.
- Return status code `201` when a book is created successfully.
- Return status code `404` when a requested book does not exist.
- Return status code `204` or a clear success response when a book is deleted.
- Return JSON error details without exposing raw database errors to the client.
