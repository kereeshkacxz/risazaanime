from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from user import User, register_user, login_user, UserDB, upload_image_user
from file import upload_image, get_image
from database import SessionLocal
import jwt
from datetime import datetime, timedelta
from starlette.middleware.cors import CORSMiddleware
import os
from studio import StudioUploader, post_studio, get_studio, get_all_studios, upload_image_studio, get_title_of_studio, Title
from title import post_title, get_title, get_all_titles, upload_image_title
from review import Review, post_review, get_review, get_all_reviews, get_review_of_titles, get_review_of_user, get_mark_of_title

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


SECRET_KEY = "RZA"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/register", response_description="Register a new user", response_model=dict)
def register(user: User, db: Session = Depends(get_db)):
    return register_user(user, db)

@app.post("/user/login", response_description="Login a user", response_model=dict)
def login(user: User, db: Session = Depends(get_db)):
    result = login_user(user, db)
    if result == True:
        token = jwt.encode(
            {"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        return {"access_token": token, "token_type": "bearer"}
    else:
        return result

@app.get("/user/me", response_model=dict)
async def read_users_me(token: str = Depends(oauth2_scheme),  db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    filepath = None
    if db_user.image_id:
        filepath = get_image(db_user.image_id, db)["filepath"]
    return {"username": username, "filepath": filepath}

@app.get("/user/get_by_username/{username}", response_model=dict)
def read_users(username: str,  db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    filepath = None
    if db_user.image_id:
        filepath = get_image(db_user.image_id, db)["filepath"]
    return {"username": username, "filepath": filepath, "reviews":get_review_of_user(username, db)}

@app.post("/user/{username}/update_image", response_description="Update user's image", response_model=dict)
def post_user_image(username: str, db: Session = Depends(get_db), file: UploadFile = File(...)):
    return upload_image_user(username, db, file)


@app.get("/statistics", response_description="Get site statistics", response_model=dict)
def statistics():
    return {"titles": 3023, "studios": 122, "reviews": 12341}

@app.post("/image/", response_description="Post the image", response_model=dict)
async def upload_image_route(folder: str, db: Session = Depends(get_db), file: UploadFile = File(...)):
    return upload_image(folder, db, file)

@app.get("/image/{image_id}", response_description="Get the image", response_model=dict)
async def get_image_route(image_id: int, db: Session = Depends(get_db)):
    return get_image(image_id, db)


@app.get("/static/{folder}/{file_name}", response_description="Get a file from static folder")
async def get_static_file(folder: str, file_name: str):
    file_path = os.path.join("static/"+folder, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.post("/studio", response_description="Post the studio", response_model=dict)
def post_studio_route(
    studio: StudioUploader, 
    db: Session = Depends(get_db),
):
    return post_studio(studio, db)

@app.get("/studio/{studio_id}", response_description="Get the studio", response_model=dict)
def get_studio_route(studio_id: int, db: Session = Depends(get_db)):
    return get_studio(studio_id, db)

@app.get("/studio", response_description="Get the studio", response_model=list[dict])
def get_studio_route(db: Session = Depends(get_db)):
    return get_all_studios(db)

@app.post("/studio/{studio_id}/update_image", response_description="Update studio's image", response_model=dict)
def post_studio_image(studio_id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    return upload_image_studio(studio_id, db, file)

@app.get("/studio/{studio_id}/titles", response_description="Get studio's titles", response_model=list[dict])
def get_title_of_studio_route(studio_id: int, db: Session = Depends(get_db)):
    return get_title_of_studio(studio_id, db)

@app.post("/title", response_description="Post the title", response_model=dict)
def post_title_route(
    title: Title, 
    db: Session = Depends(get_db),
):
    return post_title(title, db)

@app.get("/title/{title_id}", response_description="Get the title", response_model=dict)
def get_title_route(title_id: int, db: Session = Depends(get_db)):
    return get_title(title_id, db)

@app.get("/titles", response_description="Get all titles", response_model=list[dict])
def get_all_titles_route(db: Session = Depends(get_db)):
    return get_all_titles(db)

@app.post("/title/{title_id}/update_image", response_description="Update title's image", response_model=dict)
def post_title_image(title_id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    return upload_image_title(title_id, db, file)


@app.post("/review", response_description="Post the review", response_model=dict)
def post_review_route(
    review: Review, 
    db: Session = Depends(get_db),
):
    return post_review(review, db)

@app.get("/review/{review_id}", response_description="Get the review", response_model=dict)
def get_review_route(review_id: int, db: Session = Depends(get_db)):
    return get_review(review_id, db)

@app.get("/reviews", response_description="Get all reviews", response_model=list[dict])
def get_all_reviews_route(db: Session = Depends(get_db)):
    return get_all_reviews(db)

@app.get("/title/{title_id}/reviews", response_description="Get title's review", response_model=list[dict])
def get_review_of_titles_route(title_id: int, db: Session = Depends(get_db)):
    return get_review_of_titles(title_id, db)

@app.get("/user/{username}/reviews", response_description="Get user's review", response_model=list[dict])
def get_review_of_user_route(username: str, db: Session = Depends(get_db)):
    return get_review_of_user(username, db)

@app.get("/title/{title_id}/statistics", response_description="Get title's statistics", response_model=dict)
def get_mark_of_title_route(title_id: int, db: Session = Depends(get_db)):
    return get_mark_of_title(title_id, db)

@app.get("/studio/{studio_id}/statistics", response_description="Get studio's statistics", response_model=dict)
def get_mark_of_studio_route(studio_id: int, db: Session = Depends(get_db)):
    titles = get_title_of_studio(studio_id, db)
    if len(titles) == 0:
        return {"mark" : 0}
    mark = 0
    count = 0
    for i in titles:
        cur_mark = get_mark_of_title(i.get("id"), db).get("mark")
        mark += cur_mark
        if cur_mark > 0:
            count += 1
    count = max(1, count)
    return {"mark" : int(mark/count)}