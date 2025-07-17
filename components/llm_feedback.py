# 

import os
import logging
from typing import Dict, List, Optional, Any
from langchain-google-genai import ChatGoogleGenerativeAI
from components.templates import FEEDBACK_TEMPLATE
import streamlit as st

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set your API key here or use environment variable


def get_llm_feedback(resume_data: Dict[str, Any], job_role: str) -> str:
    """
    Generate LLM feedback for resume analysis
    
    Args:
        resume_data: Dictionary containing resume information with keys:
            - skills: List of skills
            - raw_text: Full resume text
            - experience_years: Years of experience (optional)
            - education: Education details (optional)
            - certifications: List of certifications (optional)
            - previous_roles: List of previous job titles (optional)
            - achievements: List of achievements (optional)
        job_role: Target job role for analysis
        
    Returns:
        String containing the LLM feedback
    """
    try:
        # Validate inputs
        if not resume_data.get("raw_text"):
            raise ValueError("Resume raw_text is required")
        if not job_role:
            raise ValueError("Job role is required")
        
        # Set up Gemini LLM
        api_key = st.secrets["api_keys"]["google"]
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-lite",  # Using latest model
            google_api_key=api_key,
            temperature=0.3,  # Lower temperature for more consistent feedback
            max_tokens=2000
        )
        
        # Prepare data for template
        skills = resume_data.get("skills", [])
        skills_text = ", ".join(skills) if skills else "None listed"
        
        # Handle optional fields
        experience_years = resume_data.get("experience_years", "Not specified")
        education = resume_data.get("education", "Not specified")
        certifications = resume_data.get("certifications", [])
        certifications_text = ", ".join(certifications) if certifications else "None listed"
        previous_roles = resume_data.get("previous_roles", [])
        previous_roles_text = ", ".join(previous_roles) if previous_roles else "Not specified"
        achievements = resume_data.get("achievements", [])
        achievements_text = ", ".join(achievements) if achievements else "None listed"
        
        # Create prompt using template
        prompt = FEEDBACK_TEMPLATE.format(
            job_role=job_role,
            skills=skills_text,
            experience_years=experience_years,
            education=education,
            certifications=certifications_text,
            previous_roles=previous_roles_text,
            achievements=achievements_text,
            raw_text=resume_data.get("raw_text", "")
        )
        
        logger.info(f"Analyzing resume for {job_role} position...")
        
        # Get LLM response
        response = llm.invoke(prompt)
        
        # Extract content
        feedback_content = response.content if hasattr(response, "content") else str(response)
        
        logger.info("Resume analysis completed successfully")
        return feedback_content
        
    except Exception as e:
        logger.error(f"Error analyzing resume: {str(e)}")
        return f"Error generating feedback: {str(e)}"

def analyze_resume_skills(resume_data: Dict[str, Any], job_role: str) -> Dict[str, List[str]]:
    """
    Additional helper function to extract specific skill analysis
    
    Args:
        resume_data: Dictionary containing resume information
        job_role: Target job role for analysis
        
    Returns:
        Dictionary with skill analysis breakdown
    """
    try:
        skills = resume_data.get("skills", [])
        
        # You can enhance this with more sophisticated skill categorization
        technical_skills = []
        soft_skills = []
        
        # Basic categorization (you can improve this)
        technical_keywords = ["python", "java", "sql", "javascript", "react", "aws", "docker", "kubernetes", "machine learning", "data science", "git", "linux"]
        soft_keywords = ["leadership", "communication", "teamwork", "problem solving", "project management", "analytical"]
        
        for skill in skills:
            skill_lower = skill.lower()
            if any(keyword in skill_lower for keyword in technical_keywords):
                technical_skills.append(skill)
            elif any(keyword in skill_lower for keyword in soft_keywords):
                soft_skills.append(skill)
            else:
                technical_skills.append(skill)  # Default to technical
        
        return {
            "technical_skills": technical_skills,
            "soft_skills": soft_skills,
            "total_skills": len(skills)
        }
        
    except Exception as e:
        logger.error(f"Error analyzing skills: {str(e)}")
        return {"technical_skills": [], "soft_skills": [], "total_skills": 0}