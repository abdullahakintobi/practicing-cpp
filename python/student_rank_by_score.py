# Variables assignment
students = {
    "Ola": 80, 
    "Ade": 50, 
    "Dele": 90, 
    "Yemi": 66, 
    "Femi": 70, 
    "Wunmi": 88
}
positions = ["1st", "2nd", "3rd", "4th", "5th", "6th"]

# Sorts students in descending order of scores
sorted_students = {k: v for k, v in sorted(students.items(), key=lambda student: student[1], reverse=True)}

print("Name: Position, score")

# Displays students with their corresponding rank and score
for student, position in zip(sorted_students.items(), positions):
    print(f"{student[0]}: {position}, {student[1]}")


# Output:
'''
Name: Position, score
Dele: 1st, 90
Wunmi: 2nd, 88
Ola: 3rd, 80
Femi: 4th, 70
Yemi: 5th, 66
Ade: 6th, 50
'''
