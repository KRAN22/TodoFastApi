from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from schemas import CreateTodo, UpdateTodo, CreateUser
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

#get Todos by user_id
@router.get("/user/{user_id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(user_id:int,db:Session=Depends(get_db)): 
    logger.info(f"get todo request received for this user_id {user_id}")   
    db_todo = db.query(model.Todo).filter(model.Todo.user_id == user_id).all()
    
    if not db_todo:
        logger.error(f"With this id {user_id} no todo Found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"With this user_id {user_id} not available todos"
                            )
    logger.info("Successfully get the all todes by user_id..")
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



#Delete todo by id
# @router.delete("/delete/{id}")
# def destroy_todo(id:int,db:Session=Depends(get_db)):
#     logger.info(f"delete todo request received for this id : {id}")
#     db_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
#     logger.info(f"{db_todo}")
#     # if not db_todo:
#     #     logger.error(f"With this id {id} no tod found")
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#     #                         detail=f"With this id {id} not available todos"
#     #                         )
    
#     # db.delete(db_todo)
#     # db.commit()
#     # logger.info("Successfully deleted the todo..")
#     return status.HTTP_204_NO_CONTENT



# #Update todo by id
# @router.put("/update/{id}")
# def update_todo(id:int,todo:UpdateTodo,db:Session=Depends(get_db)):
#     logger.info(f"update todo request received for this id : {id}")
#     db_todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    
#     if not db_todo:
#         logger.error(f"With this id {id} no todo Found")
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"With this id {id} no todos available"
#                             )
   
#     if todo.title:
#         db_todo.title = todo.title 
#     if todo.description: 
#         db_todo.description = todo.description  
#     if todo.status:
#         db_todo.status = todo.status 
        
#     db.commit()
#     db.refresh(db_todo)
#     logger.info("Successfully updated the todo...")
#     return db_todo