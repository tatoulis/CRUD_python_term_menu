class Assignments:
    def __init__(self, title):
        self.title = title


class Course:
    def __init__(self,title, stream, type):
        self.title = title
        self.stream = stream
        self.type = type
        self.assignments = []

    def add_course():
        title = input("Enter a title:")
        stream = input("Enter a stream:")
        type = input("Enter a type:")
        return Course(title,stream,type)


    def add_assignments(self, title):
        self.assignments.append(title)

    def add_Assignments():
        title = input('give the title of the assignment')
        return Assignments(title)

    def print_assignments(self):
        for i in range(len(self.assignments)):
            print(self.assignments[i].title)