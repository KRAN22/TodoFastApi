from pydantic import BaseModel
from typing import Optional


class CreateTodo(BaseModel):
    
    title : str
    description : str
    status : Optional[str] = "CREATED"
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'title':'The Dog',
                'description':'This my Gog story',
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

