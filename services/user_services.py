from repository import user_repo
import model

def getUser(db):
    queries = []
    queries.append(model.User)
    
    return user_repo.getUser(queries,db)

def getUserById(id,db):
    queries = []
    queries.append(model.User.id == id)
    
    return user_repo.getUserById(queries,db)

def createUser(user,db):
    queries = []
    queries.append(model.User.username == user.username)
    
    return user_repo.createUser(queries,user,db)

def deleteUser(id,db):
    queries = []
    queries.append(model.User.id == id)
    
    return user_repo.deleteUser(queries,db)
    