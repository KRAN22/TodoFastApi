from fastapi import APIRouter,Depends,HTTPException,status
from schemas import SignUp
from fastapi_jwt_auth.auth_jwt import AuthJWT
from sqlalchemy.orm import Session
from database import get_db
from werkzeug.security import check_password_hash
from fastapi.encoders import jsonable_encoder
from repository import user_repo
import model

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)

@router.post("/Login")
def logIn(login:SignUp,Authorize:AuthJWT=Depends(),db:Session=Depends(get_db)):
    
    if login.username:
        user = user_repo.getAllByUserName(login.username,db)
    if login.email:
        user = user_repo.getByEmail(login.email,db)
        
    if user and check_password_hash(user.password,login.password):
        access_token = Authorize.create_access_token(subject=user.username)
        refresh_token = Authorize.create_refresh_token(subject=user.username)
        
        response = {
            "access": access_token,
            'refresh': refresh_token,
        }
        return jsonable_encoder(response)
    
    raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid Authorization"
        )
    
