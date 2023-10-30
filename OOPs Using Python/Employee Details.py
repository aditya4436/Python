class Employee:
    __name=None
    __id=None
    __department=None
    
    def GetEmployeeDetails(self):
        self.__name=input("Enter the name of the employee: ")
        self.__id==input("Enter the ID of the employee: ")
        self.__department=input("Enter the department of the employee: ")
    
    def ShowEmployeeDetails(self):
        print(f"The name of the employee is: {self.__name}.")
        print(f"The ID of the employee is: {self.__id}.")
        print(f"The department of the employee is: {self.__department}.")

employee=Employee()
employee.GetEmployeeDetails()
employee.ShowEmployeeDetails()