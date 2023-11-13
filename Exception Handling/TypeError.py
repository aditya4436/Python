# TypeError:- This exception is raised when an operation or function
#             is applied to an object of the wrong type.


# The below code will throw an "TypeError", because we are
# trying to add two different types of data.

# num=11
# string="Aditya"
# sum=string+num
# print(sum)

# Now the code will not throw any error because we have handled
# the error. 
num=11
string="Aditya"
try:
    sum=num+string
except TypeError:
    print("Error: TypeError occured and handled.")