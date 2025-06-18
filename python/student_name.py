# Class in Python

class StudentName:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"Welcome {self.fname} {self.lname}!"
        
    def short(self):
        return f"The short form of your first name is {self.fname[:3].upper()}.\nAnd the short form of your last name is {self.lname[:3].upper()}."


# Test vcase       
student_1 = StudentName("Abdullah", "Akintobi")
student_2 = StudentName("Ola", "Dele")
student_3 = StudentName("Ja", "Xi")

students = [student_1, student_2, student_3]
for student in students:
    print(student)
    print(student.short(), end="\n\n")


"""
Output:

Welcome Abdullah Akintobi!
The short form of your first name is ABD.
And the short form of your last name is AKI.

Welcome Ola Dele!
The short form of your first name is OLA.
And the short form of your last name is DEL.

Welcome Ja Xi!
The short form of your first name is JA.
And the short form of your last name is XI.

"""