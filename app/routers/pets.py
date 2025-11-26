import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models import models
from app.schemas import schemas
from typing import List

router = APIRouter(prefix="/pets", tags=["Pets"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


@router.get("/", response_model=List[schemas.Pet])
def list_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).all()


@router.get("/{pet_id}", response_model=schemas.Pet)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return pet


@router.put("/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet_update: schemas.PetUpdate, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    for key, value in pet_update.dict(exclude_unset=True).items():
        setattr(pet, key, value)

    db.commit()
    db.refresh(pet)
    return pet


@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    if pet.image_path and os.path.exists(pet.image_path):
        os.remove(pet.image_path)

    db.delete(pet)
    db.commit()
    return {"message": "Pet deletado com sucesso"}


@router.post("/{pet_id}/upload", response_model=schemas.Pet)
async def upload_image(pet_id: int, image: UploadFile = File(...), db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    if pet.image_path and os.path.exists(pet.image_path):
        os.remove(pet.image_path)

    filename = f"pet_{pet_id}_{image.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(await image.read())

    pet.image_path = file_path
    db.commit()
    db.refresh(pet)
    return pet