from fastapi import FastAPI
from enum import Enum


app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}


@app.get("/book/{book_id}")
def get_book(book_id:int):
    return {"book":book_id}

@app.get("/book/list/")
def get_book_list():
    pass

