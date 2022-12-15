from fastapi import APIRouter


router = APIRouter(
    prefix= "/api/user",
    tags=["user"]
)

@router.get("/")
def hello():
    return {"Data":"Hello world"}