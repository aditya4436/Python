# Encapsulation:- It is one of the fundamental concepts in OOP. It describes
#                 the idea of wrapping data and the methods that work on data
#                 within within one unit. This puts restrictions on accessing
#                 variables and methods directly and can prevent the accidental
#                 modification of data. To prevent accidental change, an objects
#                 variable can only be changed by an object's variable can only
#                 be changed by an objects method. Those type of variables are
#                 known as private variable.
class BaseClass:
    def __init__(self):
        self.a="Aditya"
        self.__c="Pawan"
    
class DerivedClass:
    def __init__(self):
        BaseClass.__init__(self)
        print("Calling private member of base class.")
        print(self.__c)


obj=BaseClass()
print(obj.a)

# print(obj.c)
# The above line of code will give an AttributeError since we are trying to
# access the private variable from outside of the class.

# ob1=DerivedClass()
# The above code will also throw an attribute error because the private variable
# of the BaseClass is called inside the DerivedClass.