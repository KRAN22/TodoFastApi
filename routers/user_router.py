from fastapi import APIRouter,status,Depends
from schemas import CreateUser
from sqlalchemy.orm import Session
from database import get_db
from routers.todo_router import logger
import model 


router = APIRouter(
    prefix= "/api/user",
    tags=["user"]
)

# Create a User 
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(user:CreateUser,db:Session=Depends(get_db)):
    logger.info("Create user request received...")
    
    new_user = model.User(username = user.username,email=user.email, password = user.password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info("Successfully Created new user....")
    return new_user

# Get all the users from database
@router.get("/")
def get_all_users(db:Session=Depends(get_db)):
    logger.info("get user request received...")
    
    db_all_users = db.query(model.User).all() 
    
    logger.info("Successfully get all the user...")
    return db_all_users

# Get the users by id from database
# @router.get("/{id}")
# def get_user_by_id(id:int,db:Session=Depends(get_db)):
#     logger.info("get user by id reque=rst")