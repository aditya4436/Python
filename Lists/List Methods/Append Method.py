# append():- This methods add an element at the end of the list.
List=[]
n=int(input("Enter the number of list items required: "))
for i in range(0, n):
    elements=int(input(f"Enter the list item {i}: "))
    List.append(elements)
print(List)