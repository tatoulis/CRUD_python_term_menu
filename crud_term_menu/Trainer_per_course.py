class Trainer:
    def __init__(self, full_name):
        self.full_name = full_name


class Course:
    def __init__(self,title,stream,type):
        self.title = title
        self.stream = stream
        self.type = type
        self.trainers = []

    def add_course():
        title = input("Enter a title:")
        stream = input("Enter a stream:")
        type = input("Enter a type:")
        return Course(title,stream,type)


    def add_trainer(self,FullName):
        self.trainers.append(FullName)

    def add_Trainer():
        fullName = input('give the trainer full name')
        return Trainer(fullName)

    def print_trainer(self):
        for i in range(len(self.trainers)):
            print(self.trainers[i].full_name)