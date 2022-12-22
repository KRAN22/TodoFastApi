from werkzeug.security import check_password_hash
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException,status

from repository import user_repo

 
def authCreate(login,Authorize,db):
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

def authRefresh(Authorize):
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Please provide a valid refresh token"
        )
        
    current_username =  Authorize.get_jwt_subject()
    
    access_token =Authorize.create_access_token(subject=current_username)
    
    return jsonable_encoder({"access_token": access_token})