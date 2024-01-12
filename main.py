from fastapi import FastAPI

from routes import storage

app = FastAPI()

app.include_router(storage.router)
