import difflib
from collections import defaultdict, Counter
import re

ROLE_KEYWORDS = {
    'Software Engineer': {
        'skills': ['python', 'java', 'react', 'api', 'docker', 'kubernetes'],
        'experience_keywords': ['developed', 'engineered', 'built', 'deployed', 'maintained'],
        'education_keywords': ['bachelor', 'master', 'computer science', 'software engineering'],
        'weight': 1.0
    },
    'Data Scientist': {
        'skills': ['python', 'sql', 'machine learning', 'statistics', 'data visualization'],
        'experience_keywords': ['analyzed', 'modeled', 'predicted', 'visualized', 'cleaned'],
        'education_keywords': ['bachelor', 'master', 'statistics', 'data science', 'mathematics'],
        'weight': 1.2
    },
    'Product Manager': {
        'skills': ['product', 'strategy', 'stakeholder', 'roadmap', 'user research'],
        'experience_keywords': ['launched', 'managed', 'coordinated', 'led', 'planned'],
        'education_keywords': ['bachelor', 'mba', 'business', 'management'],
        'weight': 0.9
    }
}

def extract_all_text_sections(resume_data):
    """
    Merge all relevant fields into a single list of words for fuzzy matching.
    """
    sections = ['skills', 'experience', 'projects', 'education', 'certifications']
    content = []
    for section in sections:
        items = resume_data.get(section, [])
        if isinstance(items, list):
            for item in items:
                content += re.findall(r'\w+', item.lower())
        elif isinstance(items, str):
            content += re.findall(r'\w+', items.lower())
    return content

def fuzzy_match(term, content, threshold=0.8):
    """
    Fuzzy match a term against a list of words/content.
    """
    matches = difflib.get_close_matches(term.lower(), content, cutoff=threshold)
    return bool(matches)

def keyword_frequency(keywords, content):
    """
    Count the frequency of each keyword in the content.
    """
    counter = Counter(content)
    freq = {kw: counter[kw.lower()] for kw in keywords}
    return freq

def section_wise_skill_match(resume_data, required_skills):
    """
    Check which skills are found in which sections of the resume.
    """
    section_matches = defaultdict(list)
    for section, items in resume_data.items():
        if isinstance(items, list):
            section_content = ' '.join(items).lower()
        elif isinstance(items, str):
            section_content = items.lower()
        else:
            continue
        for skill in required_skills:
            if re.search(rf'\b{re.escape(skill.lower())}\b', section_content):
                section_matches[section].append(skill)
    return dict(section_matches)

def check_experience_education(resume_data, experience_keywords, education_keywords):
    """
    Check for presence of experience and education keywords in the relevant sections.
    """
    experience_section = ' '.join(resume_data.get('experience', [])) if isinstance(resume_data.get('experience'), list) else resume_data.get('experience', '')
    education_section = ' '.join(resume_data.get('education', [])) if isinstance(resume_data.get('education'), list) else resume_data.get('education', '')
    exp_found = [kw for kw in experience_keywords if re.search(rf'\b{re.escape(kw)}\b', experience_section, re.IGNORECASE)]
    edu_found = [kw for kw in education_keywords if re.search(rf'\b{re.escape(kw)}\b', education_section, re.IGNORECASE)]
    return exp_found, edu_found

def score_resume(resume_data, job_role):
    """
    Score the resume for a given job role, providing detailed breakdowns.
    """
    role_info = ROLE_KEYWORDS.get(job_role)
    if not role_info:
        return {'score': 0, 'matched_skills': [], 'missing_skills': [], 'reason': 'Unknown role'}

    required_skills = role_info['skills']
    experience_keywords = role_info.get('experience_keywords', [])
    education_keywords = role_info.get('education_keywords', [])
    weight = role_info.get('weight', 1.0)
    content = extract_all_text_sections(resume_data)

    # Skill matching
    matched = []
    missing = []
    for skill in required_skills:
        if fuzzy_match(skill, content):
            matched.append(skill)
        else:
            missing.append(skill)

    # Section-wise skill match
    section_matches = section_wise_skill_match(resume_data, required_skills)

    # Experience and education keyword checks
    exp_found, edu_found = check_experience_education(resume_data, experience_keywords, education_keywords)

    # Keyword frequency
    skill_freq = keyword_frequency(required_skills, content)

    # Scoring breakdown
    skill_score = (len(matched) / len(required_skills)) * 70  # 70% weight
    exp_score = (len(exp_found) / len(experience_keywords)) * 15 if experience_keywords else 0
    edu_score = (len(edu_found) / len(education_keywords)) * 15 if education_keywords else 0
    total_score = round((skill_score + exp_score + edu_score) * weight)

    return {
        'score': min(total_score, 100),
        'matched_skills': matched,
        'missing_skills': missing,
        'section_matches': section_matches,
        'experience_keywords_found': exp_found,
        'education_keywords_found': edu_found,
        'skill_keyword_frequency': skill_freq,
        'total_skills_required': len(required_skills),
        'match_percentage': round((len(matched) / len(required_skills)) * 100, 2),
        'scoring_breakdown': {
            'skill_score': round(skill_score, 2),
            'experience_score': round(exp_score, 2),
            'education_score': round(edu_score, 2),
            'weight': weight
        }
    }
