from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from user import User, register_user, login_user
from file import upload_image, get_image
from database import SessionLocal
import jwt
from datetime import datetime, timedelta
from starlette.middleware.cors import CORSMiddleware
import os
from studio import StudioUploader, post_studio, get_studio, get_all_studios, upload_image_studio
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
async def read_users_me(token: str = Depends(oauth2_scheme)):
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
    return {"username": username}

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
    print(file_path)
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