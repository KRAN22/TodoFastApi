from repository import todo_repo
from sqlalchemy.orm import Session
import model

def getAllTodos(user_id,title,db):
    queries = []
    if user_id:
        queries.append(model.Todo.user_id==user_id)
    if title:
        queries.append(model.Todo.title==title)

    return todo_repo.getAllTodo(queries,db)

def getTodoById(id,db):
    queries = []
    queries.append(model.Todo.id==id)

    return todo_repo.getTodoById(queries,db)

def createTodo(todo, db:Session):
    queries = []
    queries.append(model.User.id == todo.user_id)
    
    return todo_repo.createTodo(queries,todo,db)
   