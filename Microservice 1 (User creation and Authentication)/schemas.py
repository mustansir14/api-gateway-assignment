from pydantic import BaseModel, constr


class UserSchemaBase(BaseModel):

    username: constr(strip_whitespace=True, min_length=5, max_length=20)


class UserSchemaIn(UserSchemaBase):

    password: constr(strip_whitespace=True, min_length=8, max_length=20)


class UserSchemaOut(UserSchemaBase):

    id: int


class TokenSchema(BaseModel):
    access_token: str


class UserSchemaOutToken(UserSchemaOut, TokenSchema):
    pass
