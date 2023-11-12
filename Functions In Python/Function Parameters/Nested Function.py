# Nested Function:- A function that is defined inside another function is known as
#                   as the inner function or nested function. Nested functions are 
#                   able to access the variable of the enclosing scope. Inner functions
#                   are used so that they can be protected from everything happening
#                   outside the function.
def OuterFunction():
    print("This is the outer function.")
    def InnerFunction():
        print("This is the inner function.")
    InnerFunction()

OuterFunction()