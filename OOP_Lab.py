class Person(object):

    def __init__(self):
       self.name = ""
       self.age = 0
       
    def get(self):
        self.name = input("Enter the Name:")
        self.age = int(input("Age?"))
        
    def disp(self):
        print ("Name: ",self.name,"\t Age: ",self.age)

# Inherits from the class Person
class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        self.enrolNo = 0
        self.meanScore = 0.0
        
    def readStudent(self):
        super(Student,self).get()
        self.enrolNo = int(input("Enter the Enrolment Number:"))
        self.meanScore = float(input("Mean Score?"))
        
    def disp_enrolNo(self):
        print ("Enrolment Number:",self.enrolNo)
        
    def get_average(self):
        return self.meanScore