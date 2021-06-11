from fastapi import FastAPI
from pydantic import BaseModel


class Book(BaseModel):
	name: str
	price: float

app = FastAPI()

fake_books_db = [
	{ "name": "Mindset", "price": 189.0 },
	{ "name": "อิคิไก ความหมายของการมีชีวิตอยู่", "price": 250.0 },
	{ "name": "เลิกเป็นคนดี แล้วชีวิตจะมีความสุข", "price": 270.0 },
]


@app.get("/")
async def root():
	return { "message": "Hello World" }

@app.get("/books/{book_id}", response_model=Book)
async def read_books(book_id: int):
	return fake_books_db[book_id]

@app.get("/books")
async def show_all_books(skip: int = 0, limit: int = 10):
	return fake_books_db[skip: skip + limit]
	
@app.post("/books")
async def create_book(book: Book):
	fake_books_db.append(book)
	return book

