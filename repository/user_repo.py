from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
import model
import logging


logger = logging.getLogger("FastApi")

def getUser(queries,db):
    return db.query(*queries).all()

def getUserById(queries,db):
    db_user =  db.query(model.User).filter(*queries).first()   
    if not db_user:
        logger.error(f" No user Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user Found in database"
                            )
    logger.info("Successfully get the user by using id")
    return db_user

def createUser(queries,user,db:Session):
    db_user = db.query(model.User).filter(*queries).first()
    if db_user:
        logger.error("The user name is already excited..")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The userName is already excited..."
                            )
    new_user = model.User(username = user.username,
                          email=user.email,
                          password = generate_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info("Successfully Created new user....")
    return new_user