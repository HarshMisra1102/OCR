import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

try:
    from .ocr_engine import process_file
except ImportError:  # Allows running the file directly from Backend/
    from ocr_engine import process_file


app = FastAPI(title="Shayak AI OCR API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPPORTED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Shayak AI OCR API is running."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/scan")
async def scan_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file was uploaded.")

    suffix = Path(file.filename).suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Upload a PDF or image file.",
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_path = temp_file.name
            temp_file.write(await file.read())

        extracted_text = process_file(temp_path)
        return {"text": extracted_text}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process the uploaded document: {exc}",
        ) from exc
    finally:
        await file.close()

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
