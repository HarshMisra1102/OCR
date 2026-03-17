import pytesseract
from PIL import Image

# Set path if needed (Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text.strip()