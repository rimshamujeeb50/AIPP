def get_skills_score(skills):
    skill_weights = {
        'python': 10,
        'java': 8,
        'sql': 7,
        'javascript': 6,
        'html': 5,
        'css': 5
    }    
    score = 0
    for skill in skills:
        skill = skill.lower()
        if skill in skill_weights:
            score += skill_weights[skill]
    return min(score, 30)  # Cap skills score at 30
def get_experience_score(years):
    if years >= 10:
        return 30
    elif years >= 5:
        return 20
    elif years >= 2:
        return 15
    else:
        return 10
def get_education_score(level):
    education_scores = {
        'phd': 25,
        'masters': 20,
        'bachelors': 15,
        'diploma': 10
    }
    return education_scores.get(level.lower(), 5)
def get_certification_score(certifications):
    return min(len(certifications) * 5, 15)  # 5 points per certification, max 15
def main():
    print("Job Applicant Scoring System")
    print("-" * 30)
    
    # Get applicant information
    name = input("Enter applicant name: ")    
    # Get skills
    print("\nEnter skills (comma-separated):")
    skills = [skill.strip() for skill in input().split(',')]    
    # Get experience
    years_experience = float(input("\nEnter years of experience: "))    
    # Get education
    print("\nEnter highest education level (PhD/Masters/Bachelors/Diploma):")
    education = input()    
    # Get certifications
    print("\nEnter certifications (comma-separated):")
    certifications = [cert.strip() for cert in input().split(',')]    
    # Calculate scores
    skills_score = get_skills_score(skills)
    experience_score = get_experience_score(years_experience)
    education_score = get_education_score(education)
    certification_score = get_certification_score(certifications)    
    # Calculate total score (out of 100)
    total_score = skills_score + experience_score + education_score + certification_score    
    # Display results
    print("\nScoring Results for", name)
    print("-" * 30)
    print(f"Skills Score: {skills_score}/30")
    print(f"Experience Score: {experience_score}/30")
    print(f"Education Score: {education_score}/25")
    print(f"Certification Score: {certification_score}/15")
    print("-" * 30)
    print(f"Total Score: {total_score}/100")
if __name__ == "__main__":
    main()