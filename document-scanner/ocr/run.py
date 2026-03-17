from ocr.pipeline import process_document

if __name__ == "__main__":
    file_path = "sample.jpg"  # change this

    result = process_document(file_path)

    print("\n===== EXTRACTED TEXT =====\n")
    print(result["text"])