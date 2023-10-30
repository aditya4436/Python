# Private Access Modifier:- The member of the class that are declared private
#                           are accessible within the class only, private access
#                           modifier is the most secure access modifier. Data
#                           member of the class are declared private by adding
#                           a double underscore '__' symbol before the data member
#                           of that class.
class Details:
    # Below are the Private Data Members.
    __name=None
    __age=None
    __branch=None
    
    def __init__(self, name, age, branch):
        self.__name=name
        self.__age=age
        self.__branch=branch
    
    # Below is the Private Function.   
    def __Display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Branch: {self.__branch}")
    
    def DisplayDetails(self):
            self.__Display()

obj=Details("Aditya", 24, "CSE")
obj.DisplayDetails()