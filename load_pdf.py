import fitz  # PyMuPDF

def load_document(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Ganti file_path dengan lokasi file PDF yang sesuai
file_path = "Cerita rakyat-1-9-1.pdf"
document_text = load_document(file_path)

# Print first 1000 characters of the document text
print(document_text[:1000])