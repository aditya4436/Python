# Multiple Inheritence:- When a class can be derived from more than one base class
#                        this type of inheritence is known as multiple inheritence.
#                        In multiple Inheritences, all the features of the base classes
#                        are inherited into the derived class.
class BaseClass1:
    def BaseFunction1(self):
        print("This is the first base class or the first parent class.")

class BaseClass2:
    def BaseFunction2(self):
        print("This is the second base class or the second parent class.")

class DerivedClass(BaseClass1, BaseClass2):
    def DerivedFunction(self):
        print("This is the derived class or the son class.")

obj=DerivedClass()
obj.DerivedFunction()
obj.BaseFunction1()
obj.BaseFunction2()