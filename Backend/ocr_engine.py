import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OCR_PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "document-scanner"))

if OCR_PROJECT_DIR not in sys.path:
    sys.path.append(OCR_PROJECT_DIR)

from ocr.pipeline import process_document


def process_file(file_path):
    result = process_document(file_path)
    return result["text"]
