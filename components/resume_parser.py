import pdfplumber
import docx
import re

# Simple keyword-based extraction for demo
SKILL_KEYWORDS = ["python", "java", "react", "sql", "machine learning", "statistics", "product", "strategy", "stakeholder", "roadmap"]


def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text):
    found = [kw for kw in SKILL_KEYWORDS if re.search(rf"\\b{kw}\\b", text, re.IGNORECASE)]
    return list(set(found))

def parse_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        text = extract_text_from_docx(uploaded_file)
    else:
        return "", {}
    # Dummy structured extraction
    skills = extract_skills(text)
    # You can expand with more sophisticated parsing
    resume_data = {
        "skills": skills,
        "raw_text": text
    }
    return text, resume_data 