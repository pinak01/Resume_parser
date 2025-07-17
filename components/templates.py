
FEEDBACK_TEMPLATE = """
You are an expert resume reviewer and career counselor. Analyze the following resume for a {job_role} position and provide comprehensive, actionable feedback.

**RESUME INFORMATION:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 **Target Job Role:** {job_role}
🔧 **Skills Listed:** {skills}
📅 **Experience:** {experience_years} years
🎓 **Education:** {education}
🏆 **Certifications:** {certifications}
💼 **Previous Roles:** {previous_roles}
⭐ **Key Achievements:** {achievements}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**FULL RESUME TEXT:**
{raw_text}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**ANALYSIS REQUIREMENTS:**
Please provide a detailed analysis in the following format:

## 🌟 STRENGTHS
Identify 3-5 key strengths that make this candidate suitable for the {job_role} position:
- [Analyze specific skills that align with the job requirements]
- [Highlight relevant experience and achievements]
- [Note any standout qualifications or certifications]
- [Mention strong technical/soft skills combination]
- [Point out impressive career progression if applicable]

## 🔧 AREAS FOR IMPROVEMENT
Identify 3-5 specific areas where the resume could be enhanced:
- [Point out formatting or structure issues]
- [Identify missing information that employers expect]
- [Suggest improvements to make achievements more quantifiable]
- [Recommend better keyword optimization for ATS systems]
- [Note any gaps in experience or skills presentation]

## 📊 SKILL GAPS FOR {job_role}
Identify 2-4 critical skill gaps that need attention:
- [List missing technical skills essential for this role]
- [Identify soft skills that need development]
- [Suggest industry-specific knowledge areas to focus on]
- [Recommend emerging technologies or tools to learn]

## 💡 ACTIONABLE RECOMMENDATIONS
Provide 4-6 specific, actionable steps to improve job prospects:
- [Suggest specific courses, certifications, or training programs]
- [Recommend projects or experiences to gain]
- [Provide resume formatting and content improvements]
- [Suggest networking or industry engagement activities]
- [Recommend ways to better showcase existing skills]
- [Advise on preparing for common interview questions in this field]

## 📈 OVERALL ASSESSMENT
**Score: [X]/10** (where 10 = immediately hireable for target role)

**Current Standing:** [Provide 2-3 sentences summarizing the candidate's current position relative to the target role]

**Priority Actions:** [List the 2-3 most critical next steps that will have the highest impact on landing the target role]

**Timeline Recommendation:** [Suggest a realistic timeline for when the candidate might be ready to apply for the target position]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**FORMATTING GUIDELINES:**
- Be specific and actionable in all feedback
- Use professional but encouraging tone
- Focus on both technical and soft skills
- Consider ATS (Applicant Tracking System) optimization
- Prioritize improvements that will have the highest impact
- Provide concrete examples and suggestions wherever possible
- Be honest about current standing while remaining constructive

Provide detailed, constructive feedback that will genuinely help the candidate improve their chances of landing a {job_role} position.
"""

# Additional templates for specific use cases
SKILL_ANALYSIS_TEMPLATE = """
Analyze the following skills for a {job_role} position:

**Current Skills:** {skills}

Please categorize these skills and provide recommendations:

## Technical Skills Analysis:
- [List technical skills and their relevance to the role]
- [Rate each skill's importance for the position (High/Medium/Low)]
- [Identify any outdated or less relevant technical skills]

## Soft Skills Analysis:
- [List soft skills and their importance for the role]
- [Suggest ways to better demonstrate these skills]
- [Identify missing soft skills crucial for the position]

## Skill Gap Analysis:
- [List 5-7 most important missing skills for this role]
- [Prioritize which skills to learn first]
- [Suggest learning resources for each skill]

## Recommendations:
- [Provide specific steps to improve skill profile]
- [Suggest certifications or courses to pursue]
- [Recommend ways to gain practical experience]
"""

EXPERIENCE_ANALYSIS_TEMPLATE = """
Analyze the work experience for a {job_role} position:

**Experience Level:** {experience_years} years
**Previous Roles:** {previous_roles}
**Key Achievements:** {achievements}

## Experience Evaluation:
- [Assess if experience level matches job requirements]
- [Evaluate relevance of previous roles to target position]
- [Analyze career progression and growth trajectory]

## Achievement Analysis:
- [Review current achievements and their impact]
- [Suggest ways to quantify achievements better]
- [Identify missing types of achievements for the role]

## Recommendations:
- [Suggest additional experiences to gain]
- [Recommend ways to leverage current experience better]
- [Provide guidance on career progression steps]
"""