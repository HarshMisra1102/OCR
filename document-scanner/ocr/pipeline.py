import cv2
import numpy as np
from pdf2image import convert_from_path, exceptions

from ocr.preprocess import preprocess_image
from ocr.extract import extract_text
from ocr.utils import clean_text, filter_indic_text, fix_common_errors


def get_text_score(text, lang):
    if lang == "eng":
        return sum(c.isalpha() for c in text)
    elif lang == "hin":
        return sum('\u0900' <= c <= '\u097F' for c in text)
    return 0


def process_image(image, lang=None):
    processed = preprocess_image(image)

    if lang is None:
        text_hin = extract_text(processed, lang="hin")
        text_eng = extract_text(processed, lang="eng")

        score_hin = get_text_score(text_hin, "hin")
        score_eng = get_text_score(text_eng, "eng")

        text = text_hin if score_hin > score_eng else text_eng
    else:
        text = extract_text(processed, lang=lang)

    text = clean_text(text)
    text = filter_indic_text(text)
    text = fix_common_errors(text)

    return text


def process_pdf(pdf_path, lang=None):
    try:
        images = convert_from_path(pdf_path)
    except exceptions.PDFInfoNotInstalledError:
        return "PDF processing failed (Poppler not installed)."

    full_text = ""

    for img in images:
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        full_text += process_image(img, lang) + "\n"

    return full_text


def process_document(file_path, lang=None):
    if file_path.lower().endswith(".pdf"):
        text = process_pdf(file_path, lang)
    else:
        image = cv2.imread(file_path)

        if image is None:
            return {"status": "error", "text": "Invalid file"}

        text = process_image(image, lang)

    return {
        "status": "success",
        "text": text
    }