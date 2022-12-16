from fastapi import FastAPI
from routers import todo_router,user_router,Auth
from database import engine
import model
from logging.config import dictConfig
from schemas import LogConfig

dictConfig(LogConfig().dict())

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)
app.include_router(user_router.router)
app.include_router(Auth.router)

