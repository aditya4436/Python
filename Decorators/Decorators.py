# A decorators is a function that takes a function as its only parameter
# and returns a function. This is helpful to "wrap" the functionality
# with the same code over and over again.

def decorateFunction(function):
    def addHello(function2):
        return "Hello" + " " + function(function2)
    return addHello

@decorateFunction
def site(site_name):
    return site_name
print(site("Aditya"))