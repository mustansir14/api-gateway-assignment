from fastapi import FastAPI, Depends, HTTPException
from database import engine
from sqlalchemy.orm import Session
import models
import schemas
from dependencies import get_db
from sqlalchemy import select, and_
import os
from dotenv import load_dotenv
from jose import jwt, JWTError
from datetime import datetime, timedelta
load_dotenv()

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


@app.post("/signup", response_model=schemas.UserSchemaOut, status_code=201)
async def signup(user: schemas.UserSchemaIn, db: Session = Depends(get_db)):

    user_model = models.User(username=user.username, password=user.password)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return schemas.UserSchemaOut(**user_model.__dict__)


@app.post("/login", response_model=schemas.UserSchemaOutToken, status_code=200)
async def login(user: schemas.UserSchemaIn, db: Session = Depends(get_db)):

    user = db.scalar(select(models.User).where(and_(
        models.User.username == user.username, models.User.password == user.password)))
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    encode = {"sub": user.username, "id": user.id}
    expire = datetime.utcnow() + timedelta(minutes=int(os.getenv("JWT_EXPIRE_TIME_IN_MINUTES")))
    encode.update({"exp": expire})
    access_token = jwt.encode(
        encode, JWT_SECRET_KEY)
    user_with_token = schemas.UserSchemaOutToken(
        **user.__dict__, access_token=access_token)
    return user_with_token


@app.post("/decode_token", response_model=schemas.UserSchemaOut, status_code=200)
async def decode_token(token: schemas.TokenSchema):

    try:
        payload = jwt.decode(token.access_token, JWT_SECRET_KEY)
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=401, detail="Invalid username or user_id.")
        return schemas.UserSchemaOut(username=username, id=user_id)
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Could not validate credentials for user"
        )
