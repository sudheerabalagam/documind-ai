from fastapi import FastAPI
from .db import Base, engine
from .routers import documents, upload

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DocuMind AI API")

app.include_router(documents.router)
app.include_router(upload.router)


@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running"}