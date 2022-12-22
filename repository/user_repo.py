from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import model
import logging


logger = logging.getLogger("FastApi")

def getAll(queries,db):
    return db.query(*queries).all()

def getAllByUserName(username, db):
    queries = []
    queries.append(model.User.username == username)
    result =  db.query(model.User).filter(*queries).first()
    return result
    
def getByEmail(email,db):
    result = db.query(model.User).filter(model.User.email == email).first()
    return result

def getById(id,db):
    result =   db.query(model.User).filter(model.User.id == id).first()
    return result

def createUser(user,db:Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def deleteUser(id,db:Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        logger.error("The user is Not excited..")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The user is Not  excited..."
                            )
    db.delete(user)
    db.commit()
    logger.info("Successfully deleted user....")
    return status.HTTP_204_NO_CONTENT