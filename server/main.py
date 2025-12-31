from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import engine, SessionLocal
from models import Base, Video
from schemas import VideoCreate, VideoRead

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Welcome to YouQueue!"}


@app.post("/videos", response_model=VideoRead)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    db_video = Video(**video.model_dump())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


@app.get("/videos", response_model=list[VideoRead])
def list_videos(db: Session = Depends(get_db)):
    return db.query(Video).all()
