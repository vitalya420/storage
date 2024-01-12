from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from db.models import FileModel
from db.db import get_db
from utils.file_names import get_storage_filename
from repository import storage as repository_storage

router = APIRouter(prefix="/storage")


@router.get("/")
async def get_storage(db: Session=Depends(get_db)):
    return await repository_storage.get_files(db)


@router.post("/")
async def post_storage(file: UploadFile = File(), db: Session=Depends(get_db)):
    file_name = file.filename
    storage_filename = get_storage_filename(Path(file_name).stem, Path(file_name).suffix)

    with open(f"file_storage/{storage_filename}", "wb") as buffer:
        buffer.write(await file.read())

    file_model = FileModel(original_filename=file_name, storage_filename=storage_filename, created_at=datetime.now())
    return await repository_storage.post_file(db, file_model)


@router.delete("/")
async def delete_storage(file_id: int, db: Session=Depends(get_db)):
    file = await repository_storage.get_file_by_id(db, file_id)
    Path(f"file_storage/{file.storage_filename}").unlink()
    return await repository_storage.delete_file(db, file_id)