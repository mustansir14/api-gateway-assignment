from pydantic import BaseModel, constr


class TodoSchemaBase(BaseModel):

    todo: constr(strip_whitespace=True, min_length=1)


class TodoSchemaCreate(TodoSchemaBase):

    user_id: int


class TodoSchemaUpdateIn(TodoSchemaBase):

    is_completed: bool


class TodoSchemaUpdateOut(TodoSchemaUpdateIn, TodoSchemaCreate):
    pass


class TodoSchemaGet(TodoSchemaUpdateIn):

    id: int
