import pdfplumber
from docx import Document
import io

def parse_resume(filename: str, contents: bytes) -> str:
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(contents)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(contents)
    else:
        return "Unsupported file format"

def extract_text_from_pdf(contents: bytes) -> str:
    text = ""
    print('text,contents',contents,text)
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(contents: bytes) -> str:
    text = ""
    doc = Document(io.BytesIO(contents))
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text
