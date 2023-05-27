from fastapi import FastAPI
from dotenv import load_dotenv

from routes import auth, todos, news

load_dotenv()


app = FastAPI()
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(news.router)
