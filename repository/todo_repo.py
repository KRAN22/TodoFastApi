from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import logging 
import model

logger = logging.getLogger("FastApi")

def getAllTodos(user_id,title,db:Session):
    logger.info("Get todo request received....")
    queries = []
    if user_id:
        queries.append(model.Todo.user_id==user_id)
    if title:
        queries.append(model.Todo.title==title)
        
    todos = db.query(model.Todo).filter(*queries).all()
    
    if todos:
        logger.info(f"Successfully get all todos with title '{title}' and user id '{user_id}'")
        return todos
    
    logger.error(f"with this user id {user_id} and Title {title} no todos available")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"with this user id {user_id} and Title {title} no todos available"
                            )
    
def createTodo(todo,db:Session):
    logger.info("Get userTodo request received.....")
    
    db_user = db.query(model.User).filter(model.User.id == todo.user_id).first()    
    
    if not db_user:
        logger.error(f"with this id {todo.user_id} no user excited")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"with this id {todo.user_id} no user excited")
    new_todo = model.Todo(
                    title = todo.title,
                    description = todo.description,
                    user_id = todo.user_id            
                )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    
    logger.filter("Successfully created the user todo...")
    return new_todo

def getTodoById(id,db:Session):
    logger.info(f"get todo request received for this id {id}")   
    db_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    
    if not db_todo:
        logger.error(f"With this id {id} no todo Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this id {id} not available todos"
                            )
    logger.info("Successfully get the all todos by id..")
    return db_todo