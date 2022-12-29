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

    result = todo_repo.getAll(queries,db)
    return result
    
def getById(id,db):
    todo = todo_repo.getById(id,db)
    if not todo:
        logger.error(f"No Todos Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not available todos"
                            )
    logger.info("Successfully get the all todos by id..")
    return todo

def createTodo(todo,db:Session):      
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
    result = todo_repo.createTodo(new_todo,db)
    return result
    
def deleteTodo(id,db):
    result = todo_repo.deleteTodo(id, db)
    return result

def updateTodo(id,todo,db):
    current_todo = todo_repo.getById(id,db)
    # current_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    if not current_todo:
        logger.error(f"todo did't excited")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Todo not excited")
    if todo.title:
        current_todo.title = todo.title
    if todo.description:
        current_todo.description = todo.description
    if todo.status:
        current_todo.status = todo.status 
    result = todo_repo.updateTodo(current_todo,db)
    return result
        
        
    
    