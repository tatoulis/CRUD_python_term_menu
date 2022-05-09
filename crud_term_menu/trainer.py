class Trainer:

    def __init__(self,first_name,last_name,subject):
        self._first_name=first_name
        self._last_name=last_name
        self._subject=subject
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
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self,value):
        self._subject = value

class Trainer_records:
    
    def __init__(self):
        self.trainer_list = [Trainer('antonis','pappas','python')]
        
    def add_trainer_record(self,first_name,last_name,subject):
        record=Trainer(first_name,last_name,subject)
        self.trainer_list.append(record)
    
    def print_trainer_records(self):
        for item in self.trainer_list:
            print(item._first_name,item.last_name,item.subject)    
    
    

