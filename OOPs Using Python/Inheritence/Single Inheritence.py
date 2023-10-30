# Single Inheritence:- It enables us a derived class to inherit properties
#                      from a single parent class, thus enabling code 
#                      reusability and the addition of new feature to the
#                      existing code.
class ParentClass:
    def ParentFunction(self):
        print("This is the parent class")

# Here we have inherited the properties of parent class to the child class.
class ChildClass(ParentClass):
    def ChildFunction(self):
        print("This is the child class")

obj=ChildClass()
obj.ChildFunction()
obj.ParentFunction()