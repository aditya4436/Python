# Try and except statments are used to catch and handle exceptions in
# Python. Statements that can raise exceptions are kept inside the try
# clause and the statments that handle the exception are written inside
# except clause.

# The code below will throw an "IndexError", because we tried to print
# the element which is out range.

# a=[11, 2, 13]
# print("Second element = %d" %a[1])
# print("Fourth element = %d" %a[4])

# Here since we have handled the error it will not throw an error
a=[11, 2, 13]
try:
    print("Second element = %d" %a[1])
    print("Fourth element = %d" %a[4])
except:
    print("Error: IndexError occured and handled.")