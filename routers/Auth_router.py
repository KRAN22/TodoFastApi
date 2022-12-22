from fastapi_jwt_auth.auth_jwt import AuthJWT
from fastapi import APIRouter,Depends
from services import Auth_services
from sqlalchemy.orm import Session
from database import get_db
from schemas import SignUp
from logger import logger

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)

@router.post("/Login")
def logIn(login:SignUp,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    logger.info("create auth request received.....")
    result = Auth_services.authCreate(login,Authorize,db)
    logger.info("Successfully created auth_token...")
    return result
        
@router.get("/refresh")
def refresh_token(Authorize:AuthJWT=Depends()):
    logger.info("get auth_refresh request received.....")
    result = Auth_services.authRefresh(Authorize)
    logger.info("Successfully get auth_refresh Token.....")
    return result
    
