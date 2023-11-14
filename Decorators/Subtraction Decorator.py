def SubtractionDecorator(function):
    def Subtract(a, b):
        return "After subtraction the given numbers the result is: ", function(a, b)
    return Subtract

@SubtractionDecorator
def Subtracting(a, b):
    return (a-b)

print(Subtracting(5, 2))