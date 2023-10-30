# pop():- Removes and returns the last value from the list or the given index.
#         Note:- You must pass the index of the element that you want to remove.
list=[2, 4, 6, 8, 10]
print(f"The list before poping out the given element: {list}.")
index=int(input("Enter the index of the element you want to remove: "))
print(f"The list after popping out a given element from the {index} is: ")
list.pop(index)
print(list)