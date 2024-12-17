from datetime import datetime, timedelta
from fastapi import HTTPException, UploadFile, File
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from database import Base
from file import upload_image
from file import ImageDB

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    image_id = Column(String)

class User(BaseModel):
    username: str
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def register_user(user: User, db: Session):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = hash_password(user.password)
    new_user = UserDB(username=user.username, hashed_password=hashed_password, image_id="")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

def login_user(user: User, db: Session):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return True

def upload_image_user(username: str, db: Session, file: UploadFile = File(...)):
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    res = upload_image("user", db, file)
    db_user.image_id = res["id"]
    
    db.commit()
    filepath= None
    if db_user.image_id:
        image = db.query(ImageDB).filter(ImageDB.id == db_user.image_id).first()
        filepath = image.filepath if image else None 
    else:
        filepath = None 
    return {
        "username": username,
        "filepath": filepath
    }
