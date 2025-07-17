import streamlit as st
from components.resume_parser import parse_resume
from components.ats_scorer import score_resume
from components.llm_feedback import get_llm_feedback
from components.example_matcher import match_examples
from utils.file_utils import handle_upload

# Page Config
st.set_page_config(page_title="Trovex Resume Analyzer", page_icon="📄", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .big-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #4CAF50;
        }
        .sub-title {
            font-size: 1.2rem;
            color: #555;
        }
        .section-title {
            font-size: 1.5rem;
            margin-top: 20px;
            color: #333;
            border-bottom: 2px solid #4CAF50;
        }
        .stProgress > div > div > div > div {
            background-color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="big-title">📄 Trovex Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload your resume and get detailed insights, ATS score, and job-matching feedback powered by AI.</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar Inputs
with st.sidebar:
    st.header("🧾 Upload & Select")
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
    job_role = st.selectbox("Select Job Role", ["Software Engineer", "Data Scientist", "Product Manager"])

# Main Section
if uploaded_file and job_role:
    with st.spinner("🔍 Analyzing your resume..."):
        resume_text, resume_data = parse_resume(uploaded_file)
        ats_score = score_resume(resume_data, job_role)
        feedback = get_llm_feedback(resume_data, job_role)
        examples = match_examples(job_role)

    # ATS Score
    
    # LLM Feedback
    st.markdown('<div class="section-title">🧠 LLM Feedback</div>', unsafe_allow_html=True)
    st.info(feedback)

    # Example Match Suggestions


else:
    st.warning("Please upload your resume and select a job role from the sidebar to continue.")
