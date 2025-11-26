from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.models import models
from app.utils.database import engine, Base
from app.routers import pets
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Pets")

origins = [
    "http://127.0.0.1:5500",  
    "http://localhost:5500",
    "http://127.0.0.1:5501", 
    "http://localhost:5501",
    "null",                   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     
    allow_credentials=True,    
    allow_methods=["*"],      
    allow_headers=["*"],      
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(pets.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à AchaPet API!"}