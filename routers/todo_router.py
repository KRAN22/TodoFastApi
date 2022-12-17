from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from schemas import CreateTodo, UpdateTodo
import model
from database import get_db
import logging 


logger = logging.getLogger("FastApi")

router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"]
)
        
#Create to with user
@router.post("/user_todo",status_code=status.HTTP_201_CREATED)
def create_user_todo(todo:CreateTodo,db:Session=Depends(get_db)):
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
              
#Get the user todos  
@router.get("/")
def get_all_user_todo(db:Session=Depends(get_db)):
    logger.info("Get the userTodo request received....")
    db_todo = db.query(model.Todo).all()
    logger.info("Successfully get the user todos....")
    return db_todo

#get todo with todo_id
@router.get("/{todo_id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(todo_id:int,db:Session=Depends(get_db)): 
    logger.info(f"get todo request received for this id {todo_id}")   
    db_todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    
    if not db_todo:
        logger.error(f"With this id {todo_id} no todo Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this id {todo_id} not available todos"
                            )
    logger.info("Successfully get the all todos by id..")
    return db_todo

@router.get("/todoUser/")
def search_todo(user_id:int|None=None,title: str|None=None ,db:Session=Depends(get_db)):
    logger.info("get todo request received...")
    
    if user_id:
        db_todo = db.query(model.Todo).filter(model.Todo.user_id==user_id).all()
    
    if title:
        db_todo = db.query(model.Todo).filter(model.Todo.title==title).all()
    
    if user_id and title:
        db_todo = db.query(model.Todo).filter(model.Todo.title==title, model.Todo.user_id==user_id).all()
    
    if not db_todo:
        logger.error(f"With this id {user_id or title} no todo Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this user_id {user_id or title} not available todos"
                            )
    logger.info("Successfully get the all todes by user_id..")
    return db_todo