from fastapi import FastAPI
from routers import todo_router
from database import engine
import model
from logging.config import dictConfig
from schemas import LogConfig

dictConfig(LogConfig().dict())

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)

