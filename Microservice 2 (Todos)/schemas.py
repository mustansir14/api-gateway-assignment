from pydantic import BaseModel, constr


class TodoSchemaCreate(BaseModel):

    user_id: int
    todo: constr(strip_whitespace=True, min_length=1)


class TodoSchemaUpdate(TodoSchemaCreate):

    is_completed: bool


class TodoSchemaGet(TodoSchemaUpdate):

    id: int
