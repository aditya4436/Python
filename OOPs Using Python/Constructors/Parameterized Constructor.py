class SumClass:
    # Parameterized Constructor:- Constructor with parameters is known as 
    #                             parameterized constructor. The parameterized
    #                             constructor takes it first argument as a reference
    #                             to the instance being constructed known as self
    #                             and the rest of the arguments are provided by the
    #                             programmer.
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
        
a=SumClass(11, 2)
print(a.num1)
print(a.num2)