from fastapi import APIRouter,status,Depends,HTTPException
from fastapi_jwt_auth.auth_jwt import AuthJWT
from schemas import CreateUser
from sqlalchemy.orm import Session
from database import get_db
from services import user_services
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
    result = user_services.createUser(user,db)
    logger.info("Successfully created user...")
    return result

# Get all the users from database
@router.get("/")
def get_all_users(db:Session=Depends(get_db)):
    logger.info("get user request received...")
    result =  user_services.getAll(db)
    return result
    

# Get the users by id from database
@router.get("/{id}")
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    logger.info(f"Get user request received from this id {id}")
    result = user_services.getById(id,db)
    logger.info("Successfully get the user by id...")
    return result
  
@router.delete("/delete_user/{id}")
def destroy_user(id:int,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("delete user request received.....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.info(e.message)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=e.message)
    result = user_services.deleteUser(id,db)
    logger.info("Successfully delete user...")
    return result 
