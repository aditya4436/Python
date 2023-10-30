from math import pi
class Circle:
    __radius=None
    
    def __init__(self):
        self.__radius=0
    
    def GetRadius(self):
        self.__radius=int(input("Enter the area of circle: "))
    
    def ShowRadius(self):
        print(f"The radius of a circle is: {self.__radius}.")

    def AreaOfCircle(self):
        self.area=pi*self.__radius*self.__radius
        print(f"The area of the circle is: {self.area}.")

obj=Circle()
obj.GetRadius()
obj.ShowRadius()
obj.AreaOfCircle()