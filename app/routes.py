from fastapi import APIRouter
#bn3ml import l calss APIRouter from fastapi library 3lshan nnazm api endpoint fi router mostakl

from app.models import User
#han3ml import l user eli kan fi app.models 3lshan nst5dmo fi validation ll request body

router = APIRouter()
# Bennesha2 router object hanedeef 3aleh el endpoints y3ny el router dh ka2no malf aw mkan bngm3 fi el EP.

users = [
    {"name": "Ahmed", "email": "ahmed@example.com"},
    {"name": "Lydia", "email": "lydia@example.com"}
]
#di kaima mo2kta bn5zn fiha el users asna2 tash8il el application 
#Heya mesh Database; el bayanat betkoon mawgooda 
#fel memory w betedee3 lamma el application ye3mel restart

@router.get("/")
# Ben3arref GET endpoint 3ala el root path "/"
# Ay client ye3mel GET request 3ala "/" hayetnafaz el function elly ta7teha
#el request shaklo byb2a keda http://localhost:8000/

def home():
    return {"message": "Hello from my API"}

@router.get("/users")
# Ben3arref GET endpoint 3ala el root path "/users"
# Ay client ye3mel GET request 3ala "/users" hayetnafaz el function elly ta7teha
#@ di decorator bt2ol l fastapi orbot el function elly ta7t be GET 3ala el path da

def get_users():
    return users
    
@router.post("/users")
# Ben3arref POST endpoint 3ala "/users".
# El hadaf meno este2bal user gedeed men el client.

def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }