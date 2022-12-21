from repository import todo_repo
from repository import user_repo
from sqlalchemy.orm import Session
import model
from logger import logger
from fastapi import status, HTTPException


def getAll(user_id,title,db):
    queries = []
    if user_id:
        queries.append(model.Todo.user_id==user_id)
    if title:
        queries.append(model.Todo.title==title)

    return todo_repo.getAll(queries,db)

def getById(id,db):
    todo = todo_repo.getById(id,db)
    if not todo:
        logger.error(f"No Todos Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not available todos"
                            )
    logger.info("Successfully get the all todos by id..")
    return todo

def createTodo(todo, db:Session):
    user = user_repo.getById(todo.user_id,db)  
    
    if not user:
        logger.error(f"user did't excited")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"with this id {todo.user_id} no user excited")
    new_todo = model.Todo(
                    title = todo.title,
                    description = todo.description,
                    user_id = todo.user_id            
                )
    return todo_repo.createTodo(new_todo,db)

def deleteTodo(id,db):
    return todo_repo.deleteTodo(id, db)
