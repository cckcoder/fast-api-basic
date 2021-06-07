# fast-api-basic

## Presentation

* FastApi FastApi คืออะไร?
    * FastApi ทำงานอย่างไร
    * ใครเป็นคนสร้าง
    * FastApi In production

* RESTFul
    * What's RESTFul
    * มีประโยชน์อย่างไร
    * Concept of restful
        * [Ref](https://www.codecademy.com/articles/what-is-rest)

* CRUD
    * คืออะไร
        * [Ref](https://www.codecademy.com/articles/what-is-crud)

* Tools
    * VSCode Extension
        * python
        * pylance

    * pip

## Coding Time.
* Install Fast Api with pip
    * `pip install fastapi`
    * `pip install uvicorn[standard]`

* Hello world
    * [Ref](https://fastapi.tiangolo.com/tutorial/first-steps/)
    * Create simple fast-api
    ```python
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    ```
    * run api
    `uvicorn main:app --reload`

* Swagger UI
    * [go to docs](http://127.0.0.1:8000/docs)
    * [Async / Await](https://fastapi.tiangolo.com/async/#in-a-hurry)

* Path Parameters
    * get book by name
    ```python

        from fastapi import FastAPI

        app = FastAPI()


        @app.get("/books/{book_name}")
        async def read_item(book_name: str):
            return {"book_name": book_name}
    ````

* Pydantic
    * [Ref](https://fastapi.tiangolo.com/tutorial/path-params/)
    * What's pydantic
        * it's data validation
    

