def DivisionDecorator(function):
    def Division(a, b):
        return "After dividing the given numbers the result is: ", function(a, b)
    return Division

@DivisionDecorator
def Divide(a, b):
    return(a/b)

print(Divide(3, 2))