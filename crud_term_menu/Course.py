class Course:
    def __init__(self,title,stream,type,start_date,end_date):
        self._title = title
        self._stream = stream
        self._type = type
        self._start_date = start_date
        self._end_date = end_date
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        self._title = value
    @property
    def stream(self):
        return self._stream
    @stream.setter
    def stream(self,value):
        self._stream = value
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self,value):
        self._type = value
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,value):
        self._start_date = value
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self,value):
        self._end_date = value

class Course_records:
    
    def __init__(self):
        self.course_list = [Course('cb8', 'python', 'part-time', '12/10/2021','18/5/2022')]
        
    def add_course_record(self,title,stream,type,start_date,end_date):
        record=Course(title,stream,type,start_date,end_date)
        self.course_list.append(record)
    
    def print_course_records(self):
        for item in self.course_list:
            print(item.title,item.stream,item.type,item.start_date,item.end_date)