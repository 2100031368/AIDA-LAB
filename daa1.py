class Student:
    def stu(self, id, name, __cgpa):
        self.id = id
        self.name = name
        self.__cgpa = __cgpa
    def display(self):
        print(self.id,  self.name, self.__cgpa)
a = Student()
a.stu(3, "ref", 9.8)
a.display()
