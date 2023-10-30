# Class:- It is a user defined-blueprint or prototype from which the objects
#         are created. Classes provides a means of bundling or binding data
#         and the functions or methods.
class Number:
    def __init__(self):
        self.number=1
        
# Object:- The class creates a user-defined data-structure or data type, which holds its own
#          data members and member functions, which can be accessed and used by creating an
#          instance pr object of that class. A class is like a blueprint for an object.       
obj=Number()
print("The number is: ", obj.number)