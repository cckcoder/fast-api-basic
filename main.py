from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


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
async def show_all_books():
	return fake_books_db[::-1]
	
@app.post("/books")
async def create_book(book: Book):
	fake_books_db.append(book)
	return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
	book_encoded = jsonable_encoder(book)
	fake_books_db[book_id] = book_encoded
	return book_encoded

@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
	book = fake_books_db[book_id - 1]
	fake_books_db.pop(book_id - 1)
	return book
	
	

