from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///storage.db")

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()