"""
Docstring for resume
providing the % of user skills matching to the job requirement
"""

"""this Fun(match_skils)
lower all values
spliting the values of both sentenses
as we have taken it in sets we are going to do intersection 

for % we are taking it as ascore
"""
def match_skills(resume_text,job_skills):
    Resume_word=set(resume_text.lower().split())
    job_word=set(job_skills.lower().split())

    matched=Resume_word.intersection(job_word)
    score=(len(matched)/len(job_word))*100
    return matched,round(score,2)



#User input
resume=input("Give the keywords of your resume:--")
# job requirement
job="python sql ai cloud java c"

matched,score=match_skills(resume,job)


print("matched Skills",matched)
print("matched % of Score:--",score,"%")
