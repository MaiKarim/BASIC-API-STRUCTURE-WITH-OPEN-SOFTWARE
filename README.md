# Limkokwing Library API

A basic FastAPI project that simulates book search, borrowing, and returning for Limkokwing University Library.

---

## Features

- Search books by title or author
- Borrow and return system
- Asynchronous operations to handle multiple users
- Fine calculation for overdue books

---

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Async/Await Programming

---

## Installation & Setup

1. Install dependencies:
pip install fastapi uvicorn

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

---

## API Endpoints

### GET /books
Search for books

### POST /borrow
Borrow a book

### POST /return
Return a book

### GET /overdue
View overdue books

---


## Author
Maimunatu A. R. Massaquoi

---

## License
This project is for academic purposes.

---
