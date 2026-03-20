import pytesseract
import shutil

# 🔥 Auto-detect Tesseract path (works on Windows + Linux + Docker)
tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    # Optional fallback (for local Windows users)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image, lang="eng"):
    """
    Extract text from image using Tesseract OCR
    Supports multiple languages (eng, hin)
    """

    # OCR configuration
    custom_config = r'--oem 3 --psm 6'

    try:
        text = pytesseract.image_to_string(
            image,
            lang=lang,
            config=custom_config
        )
        return text

    except Exception as e:
        return f"OCR Error: {str(e)}"