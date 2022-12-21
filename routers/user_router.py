from fastapi import APIRouter,status,Depends,HTTPException
from schemas import CreateUser
from sqlalchemy.orm import Session
from database import get_db
from services import user_services
import model 
import logging


logger = logging.getLogger("FastApi")

router = APIRouter(
    prefix= "/api/user",
    tags=["user"]
)

# Create a User 
@router.post("/signIn",status_code=status.HTTP_201_CREATED)
def create_user(user:CreateUser,db:Session=Depends(get_db)):
    logger.info("Create user request received...")
    return user_services.createUser(user,db)

# Get all the users from database
@router.get("/")
def get_all_users(db:Session=Depends(get_db)):
    logger.info("get user request received...")
    return user_services.getUser(db)

# Get the users by id from database
@router.get("/{id}")
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    logger.info(f"Get user request received from this id {id}")
    return user_services.getUserById(id,db)
  
@router.delete("/delete_todo/{id}")
def destroy_todo(id:int,db:Session=Depends(get_db)):
    logger.info("delete user request received.....")
    return user_services.deleteUser(id,db)
