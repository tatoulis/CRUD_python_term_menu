import trainer, Course, student, assigment, Student_per_course, Trainer_per_course, Assignments_per_course, Assignments_per_student

trainer_list = trainer.Trainer_records()
assigment_list = assigment.assigment_record()
course_list = Course.Course_records()
student_list = student.Student_records()

# course menu!
def course_menu():
    while True:
        print("Course Menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            course_list.print_course_records()
            
    
        elif choice==2:
            title = input("Enter a title:")
            stream = input("Enter a stream:")
            type = input("Enter a type:")
            start_date = input("Enter start date")
            end_date = input("Enter end date:")
            course_list.add_course_record(title, stream, type, start_date, end_date)
    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

# trainer menu!
def trainer_menu():
    while True:
        print("Trainer Menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            trainer_list.print_trainer_records()
    
        elif choice==2:
            first_name = input("Enter a first name:")
            last_name = input("Enter a last name:")
            subject = input("Enter a subject:")
            trainer_list.add_trainer_record(first_name,last_name,subject)
    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

# student menu!
def student_menu():
    while True:
        print("Student Menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            student_list.print_student_records()
    
        elif choice==2:
            first_name = input("Enter a first name:")
            last_name = input("Enter a last name:")
            date_of_birth = input("Enter a date of birth:")
            tuition_fees = input("Enter tuition fees:")
            student_list.add_student_record(first_name, last_name, date_of_birth, tuition_fees)
    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

# assigment menu!
def assigment_menu():
    while True:
        print("Assigment Menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            assigment_list.print_assigment_records()
    
        elif choice==2:
            title = input("Enter a title:")
            description = input("Enter a description")
            sub_date = input("Enter the submitted date:")
            oral_mark = input("Enter the oral mark:")
            total_mark = input("Enter the total mark:")
            assigment_list.add_assigment_record(title, description, sub_date, oral_mark, total_mark) 
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

#Student_per_cource_menu
student_per_course_list = []
def student_per_course_menu():
    while True:
        print("Student per course menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            for item in student_per_course_list:
                print(f"The course with title:{item.title},stream: {item.stream} and type: {item.type} has this students:\n")
                item.print_students()

        elif choice==2:
            new_course = Student_per_course.Course.add_course()
            choice2 = input("Do you like to add student per course? 'y'/'n'")
            while choice2=='Y' or choice2=='y':
                new_student = Student_per_course.Course.add_Student()
                new_course.add_student(new_student)
                choice2 = input("Do you like to add student per course? 'y'/'n'")
            student_per_course_list.append(new_course)    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")
#trainer per course menu
trainer_per_course_list = []
def trainer_per_course_menu():
    while True:
        print("Trainer per course menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            for item in trainer_per_course_list:
                print(f"The course with title:{item.title},stream: {item.stream} and type: {item.type} has this trainers:\n")
                item.print_trainer()

        elif choice==2:
            new_course = Trainer_per_course.Course.add_course()
            choice2 = input("Do you like to add trainer per course? 'y'/'n'")
            while choice2=='Y' or choice2=='y':
                new_trainer = Trainer_per_course.Course.add_Trainer()
                new_course.add_trainer(new_trainer)
                choice2 = input("Do you like to add trainer per course? 'y'/'n'")
            trainer_per_course_list.append(new_course)    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")


#assignments per course menu
assignments_per_course_list = []
def assignments_per_course_menu():
    while True:
        print("Assignments per course menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            for item in assignments_per_course_list:
                print(f"The course with title:{item.title},stream: {item.stream} and type: {item.type} has this assignments:\n")
                item.print_assignments()

        elif choice==2:
            new_course = Assignments_per_course.Course.add_course()
            choice2 = input("Do you like to add trainer per course? 'y'/'n'")
            while choice2=='Y' or choice2=='y':
                new_assignment = Assignments_per_course.Course.add_Assignments()
                new_course.add_assignments(new_assignment)
                choice2 = input("Do you like to add trainer per course? 'y'/'n'")
            assignments_per_course_list.append(new_course)    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

#assignments per student menu
assignments_per_student_list = []
def assignments_per_student_menu():
    while True:
        print("Assignments per student menu")
        print("1.Get")
        print("2.Set")    
        print("3.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            for item in assignments_per_student_list:
                print(f"The student:{item.first_name} {item.last_name} has this assignments:\n")
                item.print_assignments()

        elif choice==2:
            new_student = Assignments_per_student.Students.add_student()
            choice2 = input("Do you like to add assignment per student? 'y'/'n'")
            while choice2=='Y' or choice2=='y':
                new_assignment = Assignments_per_student.Students.add_Assignments()
                new_student.add_assignments(new_assignment)
                choice2 = input("Do you like to add assignment per student? 'y'/'n'")
            assignments_per_student_list.append(new_student)    
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")


#main menu!
while True:
        print("Main menu")
        print("1.Course")
        print("2.Trainer")
        print("3.Student")    
        print("4.Assigment")
        print("5.Student per course")
        print("6.Trainer per course")
        print("7.Assignments per course")
        print("8.Assignments per student")
        print("9.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            course_menu()
    
        elif choice==2:
            trainer_menu()    
        elif choice==3:
            student_menu()
        elif choice==4:
            assigment_menu()
        elif choice==5:
            student_per_course_menu()
        elif choice==6:
            trainer_per_course_menu()
        elif choice==7:
            assignments_per_course_menu()
        elif choice==8:
            assignments_per_student_menu()
        elif choice==9:
            break
        else:
            print("Wrong Choice! Select between 1 and 5")
