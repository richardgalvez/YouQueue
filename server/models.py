from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    link = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
