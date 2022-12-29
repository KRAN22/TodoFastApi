from fastapi import APIRouter,Depends,status,HTTPException
from fastapi_jwt_auth.auth_jwt import AuthJWT
from schemas import CreateTodo,UpdateTodo
from services import todo_services
from sqlalchemy.orm import Session
from database import get_db
from .user_router import logger

router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"]
)
                  
#Get the user todos  
@router.get("/")
def get_todo(user_id:int|None=None,title: str|None=None,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("Get request received.....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.error("Required Authorization...")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Required Authorization..."
                            )
    result =  todo_services.getAll(user_id,title,db)
    logger.info(" Successfully Get todo.....")
    return result

#get todo with todo_id
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(id:int,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)): 
    logger.info("Get request received.....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.error("Required Authorization...")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Required Authorization..."
                            )
    result =  todo_services.getById(id,db)
    logger.info(" Successfully Get todo.....")
    return result

  
# Create to with user
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_todo(todo:CreateTodo,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("Create request received.....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.error("Required Authorization...")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Required Authorization..."
                            )
    result = todo_services.createTodo(todo,db)
    logger.info(" Successfully create todo.....")
    return result


@router.delete("/deleteTodo/{id}")
def destroy_todo(id:int,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("Delete Todo request received.....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.error("Required Authorization...")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Required Authorization..."
                            )
    result =  todo_services.deleteTodo(id,db)
    logger.info("Successfully Delete todo....")
    return result

@router.put("/updateTodo/{id}")
def update_todo(id:int,todo:UpdateTodo,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("Update todo request received....")
    try:
        Authorize.jwt_required()
    except Exception as e:
        logger.error("Required Authorization...")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Required Authorization..."
                            )
    result = todo_services.updateTodo(id,todo,db)
    logger.info("Successfully Updated todo....")
    return result