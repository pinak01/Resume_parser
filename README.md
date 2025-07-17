# Trovex Resume Analyzer

A modular Streamlit app for resume parsing, ATS scoring, LLM feedback (using LangChain + Gemini), and curated example matching by job role.

## Features

- Resume parsing (PDF/DOCX)
- ATS scoring (rule-based, structured comparison)
- LLM feedback (template-based, Gemini via LangChain)
- Curated resume examples by role
- Add a .streamlit folder with secrets.toml -->
  [api_keys]
  google="Your-gemini-api-key"

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Directory Structure

```
Trovex/
├── app.py
├── requirements.txt
├── README.md
├── components/
│   ├── resume_parser.py
│   ├── ats_scorer.py
│   ├── llm_feedback.py
│   ├── example_matcher.py
│   └── templates.py
├── data/
│   └── curated_examples.json
└── utils/
    └── file_utils.py
```
