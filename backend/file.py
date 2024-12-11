from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from fastapi import HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import Base
import os
from fastapi import APIRouter
import datetime
router = APIRouter()

class ImageDB(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    filepath = Column(String)

class Image(BaseModel):
    filename: str
    filepath: str

UPLOAD_DIRECTORY = "static" 

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def save_file(file: UploadFile, folder: str , new_file_name:str) -> str:
    file_location = os.path.join(UPLOAD_DIRECTORY+"/"+folder, new_file_name)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return file_location

def upload_image(folder: str, db: Session, file: UploadFile = File(...)):
    new_file_name = ''.join(file.filename.split(".")[:-1]) +'.'+ str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + '.jpg'    
    db_image = db.query(ImageDB).filter(ImageDB.filename == new_file_name).first()
    if db_image:
        raise HTTPException(status_code=400, detail="Image already uploaded")
    
    filepath = save_file(file, folder, new_file_name)
    new_image = ImageDB(filename=new_file_name, filepath=filepath)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    
    return {
        "message": "Image uploaded successfully",
        "filepath": filepath,
        "id": new_image.id 
    }


def get_image(image_id: int, db: Session):
    db_image = db.query(ImageDB).filter(ImageDB.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"filename": db_image.filename, "filepath": db_image.filepath}



