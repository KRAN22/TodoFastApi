from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from schemas import CreateTodo, UpdateTodo
import model
from database import get_db

router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"]
)

#Create a Todo
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_todo(todo:CreateTodo, db:Session=Depends(get_db)):

    #crate a model
    new_blog = model.Todo(title = todo.title,description = todo.description)
    # save to db
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#Get a all Todos     
@router.get("/",status_code=status.HTTP_200_OK)
def get_all_todos(db:Session=Depends(get_db)):
    db_todos = db.query(model.Todo).all()
    return db_todos

#get Todos by id
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(id:int,db:Session=Depends(get_db)):    
    db_todo = db.query(model.Todo).filter(model.Todo.id==id).first()
    
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this id {id} not available todos"
                            )
    else:
        return db_todo

#Delete todo by id
@router.delete("/delete/{id}")
def destroy_todo(id:int,db:Session=Depends(get_db)):
    
    db_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
        
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this id {id} not available todos"
                            )
    else:
        db.delete(db_todo)
        db.commit()
        return status.HTTP_204_NO_CONTENT

#Update todo by id
@router.put("/update/{id}")
def update_todo(id:int,todo:UpdateTodo,db:Session=Depends(get_db)):
    
    db_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this id {id} no todos available"
                            )
   
    if todo.title:
        db_todo.title = todo.title 
    if todo.description: 
        db_todo.description = todo.description  
    if todo.status:
        db_todo.status = todo.status 
    
    
    db.commit()
    
    return "successfully updated..."
        
        
        
    
        
        