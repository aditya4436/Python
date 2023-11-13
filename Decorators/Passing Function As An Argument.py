# In Python, a function can be passed as a parameter to another function
# (a function can also return another function), we can define a function
# inside another function.

# In this function we passed another function i.e., 'square'
# and a variable, i.e., 'value' and we have returned 'square'
# function and we have passed 'value' as an argument in the
# 'square' function.
def ReturnSquare(square, value):
    return square(value)

# This function returns the square of the given number.
def square(x):
    return x**2

# Here first of all 'ReturnSqaure' function is called 
# and then the 'square' function is evaluated.
result=ReturnSquare(square, 11)
print(f"The squared number is: {result}")