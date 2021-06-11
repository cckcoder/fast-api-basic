from fastapi import FastAPI
from pydantic import BaseModel
from routers import book


app = FastAPI()
app.include_router(
	book.router,
	tags=["book"]
)

@app.get("/")
async def root():
	return { "message": "Hello World" }