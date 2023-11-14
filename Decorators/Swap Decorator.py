def SwapDecorator(function):
    def Swap(a, b):
        if a>b:
            return (a-b)
        else:
            return (b-a)
    return Swap

@SwapDecorator
def Subtracting(a, b):
    return(a-b)

print(Subtracting(3, 2))