import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = os.getenv(
    "TESSERACT_PATH",
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image, lang="eng"):
    custom_config = r'--oem 3 --psm 6'

    return pytesseract.image_to_string(
        image,
        lang=lang,
        config=custom_config
    )