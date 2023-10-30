# Multilevel Inheritence:- In this inheritance, features of the base class and
#                          and derived class is further inherited into the new
#                          derived class.
class FirstGeneration:
    def FirstGenerationFunction(self):
        print("This is the first generation or the grandparent.")

class SecondGeneration(FirstGeneration):
    def SecondGenerationFunction(self):
        print("This is the second generation or the parent.")

class ThirdGeneration(SecondGeneration):
    def ThirdGenerationFunction(self):
        print("This is the third generation or the child.")

obj=ThirdGeneration()
obj.ThirdGenerationFunction()
obj.FirstGenerationFunction()
obj.SecondGenerationFunction()