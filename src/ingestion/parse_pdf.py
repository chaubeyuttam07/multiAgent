import PyPDF2

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join(page.extract_text() for page in reader.pages)
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""