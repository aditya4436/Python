# index():- Searches the tuple for the specified value and returns the
#           position of where it was found.
tuple=(21, 12, 2, 11)
n=int(input("Enter the element whose index od position you want: "))
print(tuple.index(n))

# Note:- We can use all the methods of list in tuple by coverting the
#        tuple into list and reconverting it to tuple. Let's see one
#        example:
t=(1, 2, 11, 108)
print("The elements in the tuple are: ", t)
tuple1=list(t)
tuple1.append(21)
tuple2=tuple(tuple1)
print("Tuple after converting it into list and appending an element and reconverting it to tuple: ", tuple2)