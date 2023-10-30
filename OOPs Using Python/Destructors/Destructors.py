# Destructor:- These are called when an object gets destroyed. In Python,
#              destructors are not needed as much as in C++ because Python
#              has a garbage collector that handles memory management automatically.

# The "__del__()" method is known as a destructor method in Python. It is called 
# when all references to the object have been deleted i.e., when an object is garbage
# collected.
class Destructor:
    def __init__(self):
        print("This is a default constructor.")
    
    def __del__(self):
        print("Destructor has been called.")
        
obj=Destructor()
del obj