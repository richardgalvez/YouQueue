from datetime import datetime
from pydantic import BaseModel


class VideoCreate(BaseModel):
    name: str
    link: str

class VideoRead(VideoCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
