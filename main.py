from fastapi import FastAPI
from routers import  todo_router,user_router,Auth_router
from schemas import Setting
from logging.config import dictConfig
from schemas import LogConfig
from fastapi_jwt_auth.auth_jwt import AuthJWT
from database import engine
import model


dictConfig(LogConfig().dict())

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@AuthJWT.load_config
def get_config():
    return Setting()

app.include_router(todo_router.router)
app.include_router(user_router.router)
app.include_router(Auth_router.router)


