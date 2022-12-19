from pydantic import BaseModel
from typing import Optional


class CreateTodo(BaseModel):
    
    title : str
    description : str
    status : Optional[str] = "CREATED"
    user_id : int
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'title':'The Dog',
                'description':'This my Gog story',
                "user_id": 1
            }
        }

class UpdateTodo(BaseModel):
    
    title : Optional[str]
    description : Optional[str]
    status : Optional[str]
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'title':'The Dog',
                'description':'This my Gog story',
            }
        }


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "FastApi"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "FastApi": {"handlers": ["default"], "level": LOG_LEVEL},
    }

class CreateUser(BaseModel):
    
    username : str
    email : str
    password : str
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'username':'kranthi',
                'email':'kranthi@gmail.com',
                'password': 'password'
            }
        }
       
class SignUp(BaseModel):
    
    username : str
    password : str
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'username': 'kranthi',
                'password' : 'password'
            }
        }