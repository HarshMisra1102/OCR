from ocr.pipeline import process_document
from tkinter import Tk, filedialog

if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select Document",
        filetypes=[
            ("Images", "*.png;*.jpg;*.jpeg"),
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        print("❌ No file selected!")
        exit()

    print("\n🤖 Smart OCR (Hindi + English detection)...\n")

    result = process_document(file_path)

    print("\n===== EXTRACTED TEXT =====\n")
    print(result["text"])