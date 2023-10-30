class Student:
    __name=None
    __rollno=None
    __performance=None
            
    def GetStudentDetails(self):
        self.__name=input("Enter the name of the student: ")
        self.__rollno=input("Enter the roll number: ")
        self.__performance=input("Enter the performance of the student in exam: ")
        
    def ShowStudentDetails(self):
        print(f"The name of the student is: {self.__name}.")
        print(f"The roll number of the student is: {self.__rollno}.")
        print(f"The performance of the student is: {self.__performance}.")

student1=Student()
student1.GetStudentDetails()
student1.ShowStudentDetails()      