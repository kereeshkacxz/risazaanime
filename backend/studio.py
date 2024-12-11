from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from fastapi import HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import Base
from file import upload_image
from file import ImageDB
class StudioDB(Base):
    __tablename__ = "studios"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    years_work = Column(String)
    image_id = Column(String)


class Studio(BaseModel):
    name: str
    description: str
    years_work: int
    image_id: str

class StudioUploader(BaseModel):
    name: str 
    description: str 
    years_work: str 



def post_studio(studio: StudioUploader, db: Session):
    new_studio = StudioDB(
        name=studio.name,
        description=studio.description,
        years_work=studio.years_work,
        image_id=''
    )
    db.add(new_studio)
    db.commit()
    db.refresh(new_studio)
    return {"message": "Studio registered successfully", "id": new_studio.id}


def get_studio(studio_id: int, db: Session):
    db_studio = db.query(StudioDB).filter(StudioDB.id == studio_id).first()
    if not db_studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    return {"id": db_studio.id, "name": db_studio.name, "description": db_studio.description, "years_work":db_studio.years_work, "image_id": db_studio.image_id}

def get_all_studios(db: Session):
    db_studios = db.query(StudioDB).all()  
    studios_with_images = []

    for db_studio in db_studios:
        filepath= None
        if db_studio.image_id:
            image = db.query(ImageDB).filter(ImageDB.id == db_studio.image_id).first()
            filepath = image.filepath if image else None 
        else:
            filepath = None 
        studios_with_images.append({
            "id": db_studio.id,
            "name": db_studio.name,
            "description": db_studio.description,
            "years_work": db_studio.years_work,
            "image_id": db_studio.image_id,
            "filepath": filepath  
        })

    return studios_with_images


def upload_image_studio(studio_id: int, db: Session, file: UploadFile = File(...)):
    db_studio = db.query(StudioDB).filter(StudioDB.id == studio_id).first()
    if not db_studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    
    res = upload_image("studio", db, file)
    db_studio.image_id = res["id"]
    
    db.commit()
    
    return {
        "id": db_studio.id,
        "name": db_studio.name,
        "description": db_studio.description,
        "years_work": db_studio.years_work,
        "image_id": db_studio.image_id
    }
