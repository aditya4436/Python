def SumDecorator(function):
    def AddingValues(a, b):
        return "After adding the given numbers the result is: ", function(a, b)
    return AddingValues

@SumDecorator
def Addition(a, b):
    return a+b

print(Addition(2, 3))