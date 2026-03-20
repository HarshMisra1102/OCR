import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def filter_indic_text(text):
    # Keep Indian + English characters
    text = re.sub(r'[^\u0900-\u097F\u0A80-\u0AFF\u0C80-\u0CFFa-zA-Z0-9\s]', '', text)
    return text


def fix_common_errors(text):
    replacements = {
        "ltem": "Item",
        "|tem": "Item",
        "ts italic": "is italic"
    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    return text