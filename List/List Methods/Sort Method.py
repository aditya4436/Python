# sort():- Sort a list in ascending, descending, or user-defined order.
list=[]
n=int(input("Enter the number of element you want to enter: "))
for i in range(0, n):
    element=int(input(f"Enter the element {i}: "))
    list.append(element)
print(f"The list before sorting it : {list}")
list.sort()
print(f"The list after sorting it in ascending order: {list}")
list.sort(reverse=True)
print(f"The list after sorting it in descending order: {list}")