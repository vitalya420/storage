from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FileModel(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    original_filename = Column(String)
    storage_filename = Column(String)
    created_at = Column(DateTime)