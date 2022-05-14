from pickle import NONE
from turtle import title
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from . import models
from .database import SessionLocal, engine
'''
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='IKARnamso2022',
            cursor_factory=RealDictCursor
            )
        cursor = conn.cursor()
        print("Connection successfully")
        break
    except Exception as err:
        print("Failed to connect to database")
        time.sleep(2)


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM post""")
    posts = cursor.fetchall()
    return posts

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    cursor.execute("""INSERT INTO post (title, content, published) VALUES(%s,%s,%s) RETURNING * """,(post.title, post.content,post.published))
    new_post = cursor.fetchone() 
    conn.commit()             
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("""SELECT * FROM post WHERE id=%s""",(str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )
    return post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM post WHERE id=%s returning *""",(str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )

    return {Response(status_code=status.HTTP_204_NO_CONTENT)}


@app.put("/posts/{id}")
def delete_post(id:int, post:Post):
    cursor.execute("""UPDATE post SET title=%s, content=%s, published=%s WHERE id=%s returning *""",
        (post.title, post.content,post.published, str(id)))
    updated_post = cursor.fetchone()

    conn.commit()
    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )

    return updated_post

    '''