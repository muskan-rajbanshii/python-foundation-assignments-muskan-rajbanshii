student_scores = {
    "Anisha" : 89,
    "Ravi" : 57,
    "Maya" : 92,
    "Sagar" : 61,
    "Nima" : 48
}

#Print every student and score.

for key,value in student_scores.items():
    print(f"{key} : {value}")

#Create a dictionary containing only students who scored at least 60.

new_dict = {key:value  for key, value in student_scores.items() if value >= 60}
print(new_dict)

#Find the student with the highest score.
highest_score = student_scores["Anisha"]
for key,value in student_scores.items():
    
    if value > highest_score:
        highest_score = value
        student = key

print(f"Student with Highest score is {student}:{highest_score}")

#Calculate the average score.

average_score = sum(student_scores.values())/len(student_scores)
print(f"Average score : {average_score}")