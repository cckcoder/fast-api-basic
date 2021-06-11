from fastapi import FastAPI

app = FastAPI()

fake_books_db = [
	{ "book_name": "Mindset" },
	{ "book_name": "อิคิไก ความหมายของการมีชีวิตอยู่" },
	{ "book_name": "เลิกเป็นคนดี แล้วชีวิตจะมีความสุข" },
]


@app.get("/")
async def root():
	return { "message": "Hello World" }

@app.get("/books/{book_id}")
async def read_books(book_id: int):
	return { "book_id": book_id }


@app.get("/books")
async def show_all_books(skip: int = 0, limit: int = 10):
	return fake_books_db[skip: skip + limit]
	