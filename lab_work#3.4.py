# create a list of dictionaries to store student records such as:
students = [
    {"id":101,"name":"Alice","score":85},
    {"id":102,"name":"Bob","score":78},
    {"id":103,"name":"Charlie","score":92}
    ]
# Print the name of each student using a loop.
for s in students:
    print(s["name"])
    
# Print average score of all students
a = sum(s["score"] for s in students)
print(a)
# for average 
b = a/3 # len of student
print(f"average score:{b}")

# Add a new student record to the list
students.append({"id":104,"name":"David","score":89})
print(students)

# Update the score of a student with ID 102 to 88
for s in students:
    if s["id"] == 102:
        s["score"] =88
print(students)

# delete the record of the student named "Charlie".
students.pop(2)
print(students)

# Print names of students who scored more than 80.
for s in students:
    if s["score"]>80:
        print(s["name"])
        
# sort the list of students by score (descending)
re = students[::-1]
print(re)

# Find a student with the highest score.
print( [x for x in students if x["score"] == max(s["score"] for s in students)])

# use a loop create a report in this format
# Name: Alice | Score: 85 | Grade: B
# add grading logic: A=90+, B=80-89, C<80
for s in students:
    if s["score"]>=90:
        grade="A"
    elif s["score"]>=80:
        grade="B"
    else:
        grade="C"
    print(f"Name:{s["name"]} | Score:{s["score"]} | Grade: {grade}")
    
# count how many students got each grade
for s in students:
    if s["score"]>=90:
        grade="A"
    elif s["score"]>=80:
        grade="B"
    else:
        grade="C"

# 