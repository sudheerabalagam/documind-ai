from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/")
def list_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).order_by(Document.id.desc()).all()
    return [{"id": d.id, "filename": d.filename} for d in docs]