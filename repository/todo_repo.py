from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import model
from routers.user_router import logger


def getAllTodo(queries, db):
    return db.query(model.Todo).filter(*queries).all()

def getTodoById(queries, db:Session): 
    db_todo = db.query(model.Todo).filter(*queries).first()
    
    if not db_todo:
        logger.error(f"No Todos Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not available todos"
                            )
    logger.info("Successfully get the all todos by id..")
    return db_todo

def createTodo(queries,todo,db:Session):
    db_user = db.query(model.User).filter(*queries).first()    
    
    if not db_user:
        logger.error(f"user did't excited")
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
    
    logger.info("Successfully created the user todo...")
    return new_todo

