from fastapi import FastAPI
from routers import auth_router, todo_router,user_router
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(todo_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)


