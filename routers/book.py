from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.main import BaseModel


class Book(BaseModel):
	name: str
	price: float


fake_books_db = [
	{ "name": "Mindset", "price": 189.0 },
	{ "name": "อิคิไก ความหมายของการมีชีวิตอยู่", "price": 250.0 },
	{ "name": "เลิกเป็นคนดี แล้วชีวิตจะมีความสุข", "price": 270.0 },
]

router = APIRouter()


@router.get("/books")
async def show_all_books():
	return fake_books_db[::-1]
	
@router.get("/books/{book_id}", response_model=Book)
async def read_books(book_id: int):
	return fake_books_db[book_id - 1]

@router.post("/books")
async def create_book(book: Book):
	fake_books_db.append(book)
	return book

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
	book_encoded = jsonable_encoder(book)
	fake_books_db[book_id] = book_encoded
	return book_encoded

@router.delete("/book/{book_id}")
async def delete_book(book_id: int):
	book = fake_books_db[book_id - 1]
	fake_books_db.pop(book_id - 1)