# min():- Calculates or finds the minimum element in the in the list.
# max():- Calculates or finds the maximum element in the in the list.
list=[]
n=int(input("Enter the number of elements required: "))
for i in range(0, n):
    element=int(input(f"Enter the element {i}: "))
    list.append(element)
print(f"The list is: {list}")
print(f"The minimum element in the list is: {min(list)}")
print(f"The maximum element in the list is: {max(list)}")