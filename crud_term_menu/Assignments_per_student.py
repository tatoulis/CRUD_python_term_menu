class Assignments:
    def __init__(self, title):
        self.title = title


class Students:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = []

    def add_student():
        first_name = input("Enter the first name:")
        last_name = input("Enter the last name:")
        return Students(first_name, last_name)


    def add_assignments(self, title):
        self.assignments.append(title)

    def add_Assignments():
        title = input('give the title of the assignment')
        return Assignments(title)

    def print_assignments(self):
        for i in range(len(self.assignments)):
            print(self.assignments[i].title)