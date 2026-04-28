from typing import Dict, List
import asyncio
from datetime import datetime, timedelta
app = FastAPI(title="Limkokwing Library API")

# Sample database
books: Dict[int, Dict] = {
    1: {"title": "Writing Codes", "author": "Ambrose John", "available": True},
    2: {"title": "Introduction to Python", "author": "James B. Smart", "available": True},
    3: {"title": "Learning Javascript", "author": "Amandus Coker", "available": False},
}

borrowed_books: Dict[int, Dict] = {}
@app.get("/books/search")
async def search_books(title: str | None = None, author: str | None = None) -> Dict:
    await asyncio.sleep(1)  # simulate delay
    results = [
        {"id": b_id, **info} for b_id, info in books.items()
        if (title and title.lower() in info["title"].lower()) or
           (author and author.lower() in info["author"].lower())
    ]
    return {"books": results}

@app.post("/books/borrow")
async def borrow_book(user_id: int, book_id: int) -> Dict:
    await asyncio.sleep(1)
    if books[book_id]["available"]:
        books[book_id]["available"] = False
        
        due_date = datetime.now() + timedelta(days=14)
        borrowed_books[book_id] = {"user_id": user_id, "due_date": due_date}
        return {"message": "Book borrowed successfully", "due_date": due_date.strftime("%Y-%m-%d")}
    return {"message": "Book not available"}

@app.post("/books/return")
async def return_book(user_id: int, book_id: int) -> Dict:
    await asyncio.sleep(2)
    record = borrowed_books.get(book_id)
    if record and record["user_id"] == user_id:
        books[book_id]["available"] = True
        overdue_days = (datetime.now() - record["due_date"]).days
        fine = max(0, overdue_days * 2.0)
        del borrowed_books[book_id]
        return {"message": "Book returned", "fine": fine}
    return {"message": "No such borrowing record"}


# Run using: uvicorn.run (main()):app --reload