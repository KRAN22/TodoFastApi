from repository import user_repo
from werkzeug.security import generate_password_hash
import model
from logger import logger
from fastapi import HTTPException,status

def getAll(db):
    queries = []
    queries.append(model.User)
    return user_repo.getAll(queries,db)

def getById(id,db):
    return user_repo.getById(id,db)

def createUser(user,db):
    users = user_repo.getAllByUserName(user.username,db)
    if users:
        logger.error("The user name is already excited..")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The userName is already excited..."
                            )
    new_user = model.User(username = user.username,
                          email=user.email,
                          password = generate_password_hash(user.password))
    
    return user_repo.createUser(new_user,db)

def deleteUser(id,db):    
    return user_repo.deleteUser(id,db)
    