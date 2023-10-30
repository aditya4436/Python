class Sum:
    # Protected variables
    _num1=None
    _num2=None
    _sum=None
    def __init__(self):
        self._num1=0
        self._num2=0
        
    def GetNumbers(self):
        self._num1=int(input("Enter the first number: "))
        self._num2=int(input("Enter the second number: "))

    def ShowNumbers(self):
        print(f"The first number is: {self._num1}")
        print(f"The second number is: {self._num2}")
    
    def SumFunction(self):
        self._sum=self._num1+self._num2
        print(f"The sum of the given number is: {self._sum}")
    
    def DifferenceFunction(self):
        self._sum=self._num1-self._num2
        print(f"The difference of the given number is: {self._sum}")
        
    def MultiplicationFunction(self):
        self._sum=self._num1*self._num2
        print(f"The product of the given number is: {self._sum}")
    
    def DivideFunction(self):
        self._sum=self._num1/self._num2
        print(f"The quotient of the given number is: {self._sum}")

obj=Sum()
obj.GetNumbers()
obj.ShowNumbers()
choice=(input("Enter your choice: "))
match choice:
    case '+':
        obj.SumFunction()
    case '-':
        obj.DifferenceFunction()
    case '*':
        obj.MultiplicationFunction() 
    case '/':
        obj.DivideFunction() 