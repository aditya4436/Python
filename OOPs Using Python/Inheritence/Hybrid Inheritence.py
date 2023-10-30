# Hybrid Inheritence:- Inheritence consisting of multiple types of inheritence 
# is called hybrid inheritence.
class CompanyName:
    def CompanyFunction(self):
        print("The company name is Google.")
    
class Employee1Name(CompanyName):
    def Employee1Function(self):
        print("This is the first employee.")
        
class Employee2Name(CompanyName):
    def Employee2Function(self):
        print("This is the second employee.")
  
# This class inherits the property of two classes, i.e., Employee1Name, Employee2Name.
# Therefore it is a hybrid inheritence or hybrid class.   
class Employee3Name(Employee1Name, Employee2Name):
    def Employee3Function(self):
        print("This is the third employee.")

obj=Employee3Name()
obj.Employee1Function()
obj.Employee2Function()
obj.Employee3Function()
obj.CompanyFunction()