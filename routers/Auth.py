from fastapi import APIRouter


router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
) 

@router.post("/")
def login_user():
    return "Login Successfully..."
    