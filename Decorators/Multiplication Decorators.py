def MultiplicationDecorator(function):
    def Multiply(a, b):
        return "After multiplying the given numbers the result is: ", function(a, b)
    return Multiply

@MultiplicationDecorator
def Product(a, b):
    return (a*b)

print(Product(3, 6))