from typing import List

from fastapi import FastAPI, Depends, HTTPException
from database import engine
from dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Base, Todo
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/todos/{todo_id}", response_model=schemas.TodoSchemaGet, status_code=200)
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):

    todo_model = fetch_todo_by_id(todo_id, db)
    return schemas.TodoSchemaGet(**todo_model.__dict__)


@app.get("/todos/user/{user_id}", response_model=List[schemas.TodoSchemaGet], status_code=200)
async def get_todos_by_user_id(user_id: int, db: Session = Depends(get_db)):

    todo_models = db.scalars(select(Todo).where(Todo.user_id == user_id))
    return [schemas.TodoSchemaGet(**todo.__dict__) for todo in todo_models]


@app.post("/todos", response_model=schemas.TodoSchemaGet, status_code=201)
async def create_todo(todo: schemas.TodoSchemaCreate, db: Session = Depends(get_db)):

    todo_model = Todo(**todo.__dict__)
    todo_model.is_completed = False
    add_todo_to_db(todo_model, db)
    return schemas.TodoSchemaGet(**todo_model.__dict__)


@app.put("/todos/{todo_id}", response_model=schemas.TodoSchemaGet, status_code=200)
async def update_todo_by_id(todo_id: int, todo: schemas.TodoSchemaUpdate, db: Session = Depends(get_db)):

    todo_model = fetch_todo_by_id(todo_id, db)
    for attr, value in todo.dict().items():
        setattr(todo_model, attr, value)
    add_todo_to_db(todo_model, db)
    return schemas.TodoSchemaGet(**todo_model.__dict__)


@app.delete("/todos/{todo_id}", status_code=204)
async def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):

    todo_model = fetch_todo_by_id(todo_id, db)
    db.delete(todo_model)
    db.commit()

# Helper functions


def fetch_todo_by_id(todo_id: int, db: Session) -> Todo:

    todo_model = db.scalar(select(Todo).where(Todo.id == todo_id))
    if not todo_model:
        raise HTTPException(
            status_code=404, detail="Todo with given id not found.")
    return todo_model


def add_todo_to_db(todo: Todo, db: Session) -> None:

    db.add(todo)
    db.commit()
    db.refresh(todo)
