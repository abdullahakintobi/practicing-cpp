# Variables definition
students = ["Ola", "Ade", "Dele", "Yemi", "Femi", "Wunmi"]
positions = ["1st", "2nd", "3rd", "4th", "5th", "6th"]

# Using indexing
for index in range(len(students)):
    print(f"{positions[index]}: {students[index]}")
    
print("=" * 12)

# Using zip() function
for student, position in zip(students, positions):
    print(f"{position}: {student}")

# Output:
'''
1st: Ola
2nd: Ade
3rd: Dele
4th: Yemi
5th: Femi
6th: Wunmi
============
1st: Ola
2nd: Ade
3rd: Dele
4th: Yemi
5th: Femi
6th: Wunmi
'''
