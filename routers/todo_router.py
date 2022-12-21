from fastapi import APIRouter,Depends,status
from schemas import CreateTodo
from services import todo_services
from sqlalchemy.orm import Session
from database import get_db
from .user_router import logger

router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"]
)
                  
#Get the user todos  
@router.get("/")
def get_todo(user_id:int|None=None,title: str|None=None,db:Session=Depends(get_db)):
    logger.info("Get userTodo request received.....")
    return todo_services.getAllTodos(user_id,title,db)

#get todo with todo_id
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(id:int,db:Session=Depends(get_db)): 
    return todo_services.getTodoById(id,db)
  
# Create to with user
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_todo(todo:CreateTodo,db:Session=Depends(get_db)):
    logger.info("Get userTodo request received.....")
    return todo_services.createTodo(todo,db)

@router.delete("/deleteTodo/{id}")
def destroy_todo(id:int,db:Session=Depends(get_db)):
    logger.info("Delete Todo request received.....")
    return todo_services.deleteTodo(id,db)