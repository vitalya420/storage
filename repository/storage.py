from sqlalchemy.orm import Session

from db.models import FileModel as FileModel


async def get_files(db: Session):
    return db.query(FileModel).all()


async def get_file_by_id(db: Session, file_id: int):
    return db.query(FileModel).filter(FileModel.id == file_id).first()


async def post_file(db: Session, file: FileModel):
    db.add(file)
    db.commit()
    db.refresh(file)
    return file


async def delete_file(db: Session, file_id: int):
    file = await get_file_by_id(db, file_id)
    db.delete(file)
    db.commit()
    return {"message": "File deleted successfully"}