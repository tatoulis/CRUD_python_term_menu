class Student:
    def __init__(self, full_name):
        self.full_name = full_name


class Course:
    def __init__(self,title,stream,type):
        self.title = title
        self.stream = stream
        self.type = type
        self.students = []

    def add_course():
        title = input("Enter a title:")
        stream = input("Enter a stream:")
        type = input("Enter a type:")
        return Course(title,stream,type)


    def add_student(self,FullName):
        self.students.append(FullName)

    def add_Student():
        fullName = input('give the student full name')
        return Student(fullName)

    def print_students(self):
        for i in range(len(self.students)):
            print(self.students[i].full_name)