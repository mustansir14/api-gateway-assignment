from typing import List

from fastapi import APIRouter, Depends

from dependencies import get_current_user
from schemas.todo import TodoSchemaGet, TodoSchemaBase, TodoSchemaUpdateIn, TodoSchemaUpdateOut, TodoSchemaCreate
from schemas.user import UserSchemaOut
from services import todos_service

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("", response_model=List[TodoSchemaGet], status_code=200)
async def get_all_todos_for_logged_in_user(user: UserSchemaOut = Depends(get_current_user)):
    return todos_service.get_todos_for_logged_in_user(user.id)


@router.get("/{todo_id}", response_model=TodoSchemaGet, status_code=200)
async def get_todo_by_id(todo_id: int, user: UserSchemaOut = Depends(get_current_user)):
    return todos_service.get_todo_by_id(todo_id)


@router.post("", response_model=TodoSchemaGet, status_code=201)
async def create_todo(todo: TodoSchemaBase, user: UserSchemaOut = Depends(get_current_user)):
    return todos_service.create_todo(TodoSchemaCreate(**todo.dict(), user_id=user.id))


@router.put("/{todo_id}", response_model=TodoSchemaGet, status_code=200)
async def update_todo(todo_id: int, todo: TodoSchemaUpdateIn, user: UserSchemaOut = Depends(get_current_user)):
    return todos_service.update_todo_by_id(todo_id, todo=TodoSchemaUpdateOut(**todo.dict(), user_id=user.id))


@router.delete("/{todo_id}", response_model=None, status_code=200)
async def delete_todo(todo_id: int, user: UserSchemaOut = Depends(get_current_user)):
    return todos_service.delete_todo_by_id(todo_id)
