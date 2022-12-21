from sqlalchemy.orm import Session
import model
from logger import logger
from fastapi import status, HTTPException


def getAll(queries, db):
    return db.query(model.Todo).filter(*queries).all()

def getById(id, db:Session): 
    return db.query(model.Todo).filter(model.Todo.id==id).first()

def createTodo(todo,db:Session):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def deleteTodo(id,db:Session):
    todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    if not todo:
        logger.error("The Todo is Not excited..")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The Todo is Not  excited..."
                            )
    db.delete(todo)
    db.commit()
    return status.HTTP_204_NO_CONTENT
