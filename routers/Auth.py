from fastapi import APIRouter
from schemas import SignUp
import model
from fastapi_jwt_auth.auth_jwt import AuthJWT

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
) 

@router.post("/")
def login_user():
    return "Login Successfully..."
    