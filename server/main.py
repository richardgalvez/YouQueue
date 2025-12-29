from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

video_list = []

class Video(BaseModel):
    id: int
    name: str
    link: str
    created_at: datetime

@app.get("/")
def home():
    message = "Welcome to YouQueue!"
    return {"Message": message}

# TODO: Show list of current videos
@app.get("/videos")
def get_video_list():
    return video_list

# TODO: Add videos to list of current videos
@app.post("/videos")
def add_videos(video: Video):
    video_list.insert(video.id, video.name)
    return {"Current List of Videos": video_list}
