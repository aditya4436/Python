# In Python every variable name is a reference. When we pass a varibale to
# a function, a new reference to the object is created.
def Function(num):
    num[0]=10

list=[20, 22, 39, 56, 75]
# The element at the first index is updated or changed.
Function(list)
print(f"The updated list is: {list}.")