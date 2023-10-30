# Hierarchical Inheritence:- When more than one derived classes are created from
#                            single base class this type of inheritence is called
#                            hierarchical inheritence.
class ParentClass:
    def ParentClassFunction(self):
        print("This is the parent class.")

class FirstChildClass(ParentClass):
    def FirstChildFunction(self):
        print("This is the first child class.")

class SecondChildClass(ParentClass):
    def SecondChildFunction(self):
        print("This is the second child class.")

obj1=FirstChildClass()
obj2=SecondChildClass()
print("Below is created from from First Child Class.")
obj1.ParentClassFunction()
obj1.FirstChildFunction()
print("\nBelow is created from from Second Child Class.")
obj2.ParentClassFunction()
obj2.SecondChildFunction()