from typing import List

from services.client import make_request
from schemas.todo import TodoSchemaGet, TodoSchemaCreate, TodoSchemaUpdateOut

import os

TODOS_API = os.getenv("TODOS_API")


def get_todo_by_id(id: int) -> TodoSchemaGet:
    return make_request("GET", TODOS_API + f"/todos/{id}", data={}, success_code=200, response_schema=TodoSchemaGet)


def get_todos_for_logged_in_user(user_id: int) -> List[TodoSchemaGet]:
    return make_request("GET", TODOS_API + f"/todos/user/{user_id}", data={}, success_code=200, response_schema=TodoSchemaGet, respone_is_list=True)


def create_todo(todo: TodoSchemaCreate) -> TodoSchemaGet:
    return make_request("POST", TODOS_API + f"/todos", data=todo.dict(), success_code=201, response_schema=TodoSchemaGet)


def update_todo_by_id(id: int, todo: TodoSchemaUpdateOut) -> TodoSchemaGet:
    return make_request("PUT", TODOS_API + f"/todos/{id}", data=todo.dict(), success_code=200, response_schema=TodoSchemaGet)


def delete_todo_by_id(id: int) -> None:
    make_request("DELETE", TODOS_API +
                 f"/todos/{id}", data={}, success_code=204, response_schema=None)
