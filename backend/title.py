from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel, Field
from fastapi import HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import Base
from file import upload_image
from file import ImageDB
from studio import StudioDB, TitleDB, Title



def post_title(title: Title, db: Session):
    new_title = TitleDB(
        name=title.name,
        description=title.description,
        episodes=title.episodes,
        image_id="",
        episode_duration=title.episode_duration,
        status=title.status,
        studio_id=title.studio_id,
    )
    db.add(new_title)
    db.commit()
    db.refresh(new_title)
    return {"message": "Title registered successfully", "id": new_title.id}

def get_title(title_id: int, db: Session):
    db_title = db.query(TitleDB).filter(TitleDB.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    
    filepath = None
    if db_title.image_id:
        image = db.query(ImageDB).filter(ImageDB.id == db_title.image_id).first()
        filepath = image.filepath if image else None 
    
    return {
        "id": db_title.id,
        "name": db_title.name,
        "description": db_title.description,
        "episodes": db_title.episodes,
        "image_id": db_title.image_id,
        "episode_duration": db_title.episode_duration,
        "status": db_title.status,
        "filepath": filepath,
        "studio_id": db_title.studio_id
    }

def get_all_titles(db: Session):
    db_titles = db.query(TitleDB).all()  
    titles_with_images = []

    for db_title in db_titles:
        filepath = None
        if db_title.image_id:
            image = db.query(ImageDB).filter(ImageDB.id == db_title.image_id).first()
            filepath = image.filepath if image else None 
        
        titles_with_images.append({
            "id": db_title.id,
            "name": db_title.name,
            "description": db_title.description,
            "episodes": db_title.episodes,
            "image_id": db_title.image_id,
            "episode_duration": db_title.episode_duration,
            "status": db_title.status,
            "filepath": filepath  
        })

    return titles_with_images

def upload_image_title(title_id: int, db: Session, file: UploadFile = File(...)):
    db_title = db.query(TitleDB).filter(TitleDB.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    
    res = upload_image("title", db, file)
    db_title.image_id = res["id"]
    
    db.commit()
    filepath = None
    if db_title.image_id:
        image = db.query(ImageDB).filter(ImageDB.id == db_title.image_id).first()
        filepath = image.filepath if image else None 
    
    return {
        "id": db_title.id,
        "name": db_title.name,
        "description": db_title.description,
        "episodes": db_title.episodes,
        "image_id": db_title.image_id,
        "episode_duration": db_title.episode_duration,
        "status": db_title.status,
        "filepath": filepath  
    }
