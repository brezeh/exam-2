#exam 2 breze howard

class Student:
    def __init__(self, studentid, name, score):
        self.studentid = studentid
        self.name = name
        self.score = score

    def __str__(self):
        return f"ID: {self.studentid}, Name: {self.name}, Score: {self.score}"

#add a student
def addstudent(studentlist, student):
    studentlist.append(student)

#search for a student
def searchstudent(studentlist, studentid):
    for student in studentlist:
        if student.studentid == studentid:
            return str(student)
    return "Student not found"

#sort students by score
def sortstudents(studentlist):
    return sorted(studentlist, key=lambda student: student.score, reverse=True)

#student list
students = [
    Student(1, "Alice", 85),
    Student(2, "Bendy", 90),
    Student(3, "Charlie", 78)
]

#example
print("Initial list of students:")
for student in students:
    print(student)

#adding a new student
newstudent = Student(4, "Alastor", 92)
addstudent(students, newstudent)
print("\nAfter adding a new student:")
for student in students:
    print(student)

#sorting students by score
sortedstudents = sortstudents(students)
print("\nSorted list of students by score (descending):")
for student in sortedstudents:
    print(student)

#searching for a student 
searchresult = searchstudent(students, 2)
print("\nSearch result for student ID 2:")
print(searchresult)

#searching for a student that doesn't exist
searchresult = searchstudent(students, 5)
print("\nSearch result for student ID 5:")
print(searchresult)