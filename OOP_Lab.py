class Person(object):

    def __init__(self):
       self.name = " "
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
        self.course = ""
        self.__enrolNo = 0
        self.__enrolYear = 0
        self.meanScore = 0.0
        
    def readStudent(self):
        super(Student,self).get()
        self.enrolNo = int(input("Enter the Enrolment Number: "))
        self._enrolYear = int(input("Enter year of enrolment: "))
        self.meanScore = float(input("Mean Score? "))
        self.course = input("Course of Study: ")
        
    def disp_enrolDetails(self):
        print ("Enrolment number {0} is registered for course {1} ".format(self.enrolNo, self.course))
        
    def get_average(self):
        return self.meanScore
        
class GradStudent(Student):

    def __init__(self):
        super(GradStudent, self).__init__()
        self.underGradCourse = " "
        self.matriculation = 0

    def check_if_matriculated_before_enrolling(self):
        if _Student__enrolYear < self.matriculation:
            print ('A new graduate student must be matriculated before enrolment')
        else:
            print ('Student can be enrolled')