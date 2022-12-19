from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from schemas import CreateTodo, UpdateTodo
from repository.todo_repo import getAllTodos,createTodo,getTodoById
import model
from database import get_db
import logging 


logger = logging.getLogger("FastApi")

router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"]
)
        
#Create to with user
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_todo(todo:CreateTodo,db:Session=Depends(get_db)):
    return createTodo(todo,db)
              
#Get the user todos  
@router.get("/")
def get_todo(user_id:int|None=None,title: str|None=None ,db:Session=Depends(get_db)):
    return  getAllTodos(user_id,title,db)

#get todo with todo_id
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(id:int,db:Session=Depends(get_db)): 
    return getTodoById(id,db)
  
