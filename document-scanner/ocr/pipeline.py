import numpy as np
import cv2
from pdf2image import convert_from_path

from ocr.preprocess import preprocess_image
from ocr.extract import extract_text
from ocr.utils import clean_text


def process_image(image):
    processed = preprocess_image(image)
    text = extract_text(processed)
    return clean_text(text)


def process_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    full_text = ""

    for img in images:
        img_cv = cv2.cvtColor(
            cv2.imread(img.filename) if hasattr(img, "filename") else
            cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR),
            cv2.COLOR_BGR2RGB
        )
        full_text += process_image(img_cv) + "\n"

    return full_text


def process_document(file_path):
    if file_path.lower().endswith(".pdf"):
        text = process_pdf(file_path)
    else:
        image = cv2.imread(file_path)
        text = process_image(image)

    return {
        "status": "success",
        "text": text
    }