from fastapi import APIRouter
from app.models import User

router = APIRouter()

users = [
    {"name": "Ahmed", "email": "ahmed@example.com"},
    {"name": "Lydia", "email": "lydia@example.com"}
]

@router.get("/")
def home():
    return {"message": "Hello from my API"}

@router.get("/users")
def get_users():
    return users
    
@router.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }