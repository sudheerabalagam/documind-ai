import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Document
from ..config import settings
from ..services.pdf_service import extract_text_from_pdf

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    os.makedirs(settings.upload_dir, exist_ok=True)
    stored_path = os.path.join(settings.upload_dir, file.filename)

    with open(stored_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(stored_path)

    document = Document(
        filename=file.filename,
        stored_path=stored_path,
        extracted_text=extracted_text,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "Document uploaded successfully",
        "document_id": document.id,
        "filename": document.filename,
    }