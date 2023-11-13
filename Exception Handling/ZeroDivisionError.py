# ZeroDivisionError:- This exception occurs when an attempt is made
#                     to divide a number by zero.
def function(a):
    if(a<4):
        b=a/(a-3)
    print("Value of b is: ", b)

try:
    function(3)
    function(5)
except ZeroDivisionError:
    print("Error: ZeroDivisionError and handled.")