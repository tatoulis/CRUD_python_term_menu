class Assigment:
    def __init__(self,title,description,subDateTime,oralMark,totalMark):
        self._title = title
        self._description = description
        self._subDateTime = subDateTime
        self._oralMark = oralMark
        self._totalMark = totalMark
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        self._title = value
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,value):
        self._description = value
    @property
    def subDateTime(self):
        return self._subDateTime
    @subDateTime.setter
    def subDateTime(self,value):
        self._subDateTime = value
    @property
    def oralMark(self):
        return self._oralMark
    @oralMark.setter
    def oralMark(self,value):
        self._oralMark = value
    @property
    def totalMark(self):
        return self._totalMark
    @totalMark.setter
    def totalMark(self,value):
        self._totalMark = value

class assigment_record:

    def __init__(self):
        self.assigment_list = [Assigment('project_1', 'for python', '10/12/2021', '10', '100')]

    def add_assigment_record(self, title, description, subDateTime, oralMark, totalMark):
        record = Assigment(title, description, subDateTime, oralMark, totalMark)
        self.assigment_list.append(record)

    def print_assigment_records(self):
        for item in self.assigment_list:
            print(item.title, item.description, item.subDateTime, item.oralMark, item._totalMark)