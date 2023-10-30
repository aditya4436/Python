# Data Abstraction:- Data Abstraction in Python is a programming  concept that hides
#                    the complex implementation details while exposing the only essential
#                    information and functionalities to users. In Python, we can achieve
#                    data abstraction by using abstract classes and abstract classes can 
#                    be created using 'abc' i.e., 'abstract' base class module and
#                    'abstractmethod' of 'abc' module.
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
    
    @abstractmethod
    def PrintDetails(self):
        pass
    
    def Accelerate(self):
        print("Speeds up the car.")

class Hatchback(Car):
    def PrintDetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
    
    def SunRoof(self):
        print("This feature is not available")

class SUV(Car):
    def PrintDetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
    
    def SunRoof(self):
        print("This feature is available.")

car1=Hatchback("Maruti", "Alto", 2022)
car1.PrintDetails()
car1.SunRoof()

car2=SUV("Hyundai", "Tucson", 2021)
car2.PrintDetails()
car2.SunRoof()