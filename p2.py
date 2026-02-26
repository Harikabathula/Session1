def match_skills(resume_text, job_skills):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_skills.lower().split())

    matched = resume_words.intersection(job_words)
    score = (len(matched) / len(job_words)) * 100
    return matched, round(score, 2)

# Example input
resume = "python machine learning data science sql"
job = "python sql ai machine learning cloud"

matched, score = match_skills(resume, job)

print("Matched Skills:", matched)
print("Match Score:", score, "%")
