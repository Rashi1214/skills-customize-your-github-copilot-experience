# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice web routes, JSON data, request validation, and HTTP status codes. You will create an API for managing a collection of books.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Use the provided starter code to create a FastAPI application and run it with Uvicorn.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Start the application with Uvicorn.
- Return a welcome message from the root route, `/`.
- Make the interactive API documentation available at `/docs`.

### 🛠️ Implement Book Routes

#### Description

Add REST routes that allow clients to read and create books in an in-memory collection.

#### Requirements

Completed program should:

- Return all books from `GET /books`.
- Return one book from `GET /books/{book_id}`.
- Add a new book with `POST /books`.
- Return a helpful response when a requested book does not exist.

Example request:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

Example response:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Add Validation and Status Codes

#### Description

Define a Pydantic model for incoming books and make the API respond with appropriate validation errors and HTTP status codes.

#### Requirements

Completed program should:

- Require both `title` and `author` when creating a book.
- Reject empty or missing book fields with a validation response.
- Return status code `201` when a book is created successfully.
- Return status code `404` when a book cannot be found.
- Return JSON responses with clear error details.
