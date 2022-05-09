class Student:
    def __init__(self,first_name,last_name,date_of_birth,tuitionFees):
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._tuitionFees = tuitionFees
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,value):
        self._first_name = value
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,value):
        self._last_name = value
    @property
    def date_of_birth(self):
        return self._date_of_birth
    @date_of_birth.setter
    def date_of_birth(self,value):
        self._date_of_birth = value
    @property
    def tuitionFees(self):
        return self._tuitionFees
    @tuitionFees.setter
    def tuitionFees(self,value):
        self._tuitionFees = value

class Student_records:
    
    def __init__(self):
        self.student_list = [Student('kleanthis', 'tsaousis', '10/02/1989', '2000')]
        
    def add_student_record(self,first_name,last_name,date_of_birth,tuitionFees):
        record=Student(first_name,last_name,date_of_birth,tuitionFees)
        self.student_list.append(record)
    
    def print_student_records(self):
        for item in self.student_list:
            print(item._first_name,item.last_name,item.date_of_birth,item.tuitionFees)    
