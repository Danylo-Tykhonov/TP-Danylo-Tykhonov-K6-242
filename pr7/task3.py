class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


class StudentData:
    def __init__(self, students):
        self.students = students

    def sort_students(self, column):
        if column == "name":
            sorted_students = sorted(self.students, key=lambda student: student.name)
            print("\nSorted by name:\n")

        elif column == "age":
            sorted_students = sorted(self.students, key=lambda student: student.age)
            print("\nSorted by age:\n")

        else:
            print("\Incorect column. Try again\n")
            return

        for student in sorted_students:
            print(student)



students = [
    Student('Daria', 18),
    Student('Oleh', 19),
    Student('Sofia', 20),
    Student('Mark', 22),
    Student('Iryna', 21),
    Student('Tim', 23),
    Student('Helena', 19),
    Student('Leon', 24),
    Student('Karina', 20),
    Student('Robert', 26)
]

while True:
    column = input("Choose the column (name, age): ")
    if column in ("name", "age"):
        break
    else:
        print("\nSomething went wrong\n")

student_data = StudentData(students)
student_data.sort_students(column)