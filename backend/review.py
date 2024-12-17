from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel, Field
from fastapi import HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import Base
from file import upload_image
from file import ImageDB
from title import TitleDB
from user import UserDB

mark_system = [1.00, 1.0675, 1.1349, 1.2024, 1.2699, 1.3373, 1.4048, 1.4723, 1.5397, 1.6072]

class ReviewDB(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    title_id = Column(Integer, ForeignKey(TitleDB.id), index=True) 
    username = Column(String)
    vibe = Column(Integer) 
    plot = Column(Integer)
    characters = Column(Integer) 
    drawing = Column(Integer) 
    music = Column(Integer) 
    mark = Column(Integer) 
    description = Column(String)
    title = Column(String)

class Review(BaseModel):
    title_id: int
    username: str
    vibe: int
    plot: int
    characters: int
    drawing: int
    music: int
    description: str
    title: str

def post_review(review: Review, db: Session):
    for i in ["vibe", "plot", "characters", "music", "drawing"]:
        value = getattr(review, i)
        if value > 10 or value < 1:
            raise HTTPException(status_code=400, detail=f"Value for {i} must be between 1 and 10")
    
    # Ensure that vibe is within the range of mark_system
    if review.vibe < 1 or review.vibe > len(mark_system):
        raise HTTPException(status_code=400, detail="Vibe must be between 1 and {}".format(len(mark_system)))

    new_review = ReviewDB(
        title_id=review.title_id,
        username=review.username,
        vibe=review.vibe,
        plot=review.plot,
        characters=review.characters,
        drawing=review.drawing,
        music=review.music,
        description=review.description,
        title=review.title,
        mark=int((review.music + review.drawing + review.plot + review.characters) * 1.4 * mark_system[review.vibe - 1]),
    )
    
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return {"message": "Review registered successfully", "id": new_review.id}



def get_review(review_id: int, db: Session):
    db_review = db.query(ReviewDB).filter(ReviewDB.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Studio not found")
    return {
        "title_id":db_review.title_id,
        "username":db_review.username,
        "vibe":db_review.vibe,
        "plot":db_review.plot,
        "characters":db_review.characters,
        "drawing":db_review.drawing,
        "music":db_review.music,
        "description":db_review.description,
        "title":db_review.title,
        "mark":db_review.mark
    }


def get_all_reviews(db: Session):
    db_reviews = db.query(ReviewDB).all()  
    reviews = []

    for db_review in db_reviews:
        reviews.append({
        "title_id":db_review.title_id,
        "username":db_review.username,
        "vibe":db_review.vibe,
        "plot":db_review.plot,
        "characters":db_review.characters,
        "drawing":db_review.drawing,
        "music":db_review.music,
        "description":db_review.description,
        "title":db_review.title,
        "mark":db_review.mark
        })

    return reviews

def get_review_of_titles(title_id: int, db: Session):
    db_title = db.query(TitleDB).filter(TitleDB.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    
    reviews = db.query(ReviewDB).filter(ReviewDB.title_id == title_id).all()
    reviews_list = []
    for db_review in reviews:
        reviews_list.append({
        "title_id":db_review.title_id,
        "username":db_review.username,
        "vibe":db_review.vibe,
        "plot":db_review.plot,
        "characters":db_review.characters,
        "drawing":db_review.drawing,
        "music":db_review.music,
        "description":db_review.description,
        "title":db_review.title,
        "mark":db_review.mark
        })
    
    return reviews_list

def get_review_of_user(username: int, db: Session):
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    reviews = db.query(ReviewDB).filter(ReviewDB.username == username).all()
    reviews_list = []
    for db_review in reviews:
        reviews_list.append({
        "title_id":db_review.title_id,
        "username":db_review.username,
        "vibe":db_review.vibe,
        "plot":db_review.plot,
        "characters":db_review.characters,
        "drawing":db_review.drawing,
        "music":db_review.music,
        "description":db_review.description,
        "title":db_review.title,
        "mark":db_review.mark
        })
    
    return reviews_list

def get_mark_of_title(title_id: int, db: Session):
    db_title = db.query(TitleDB).filter(TitleDB.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    
    reviews = db.query(ReviewDB).filter(ReviewDB.title_id == title_id).all()
    count = 0
    marks ={
        "vibe":0,
        "plot":0,
        "characters":0,
        "drawing":0,
        "music":0,
        "mark":0
        }
    for db_review in reviews:
        marks["vibe"] += db_review.vibe
        marks["plot"] += db_review.plot
        marks["drawing"] += db_review.drawing
        marks["music"] += db_review.music
        marks["mark"] += db_review.mark
        marks["characters"] += db_review.characters
        count += 1
    if count == 0:
        return marks 
    else:
        marks["vibe"] = int(marks["vibe"]/count)
        marks["plot"] = int(marks["plot"]/count)
        marks["drawing"] = int(marks["drawing"]/count)
        marks["music"] = int(marks["music"]/count)
        marks["mark"] = int(marks["mark"]/count)
        marks["characters"] = int(marks["characters"]/count)
    return marks