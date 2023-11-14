def Swap(l, a, b):
    temp=l[a]
    l[a]=l[b]
    l[b]=temp
    return l

list=[]
n=int(input("Enter the number of elements you want in a list: "))
for i in range(0, n):
    elements=int(input(f"Enter the element {i}: "))
    list.append(elements)
print(f"The list after inserting the elements in the list: {list}")
index1=int(input(f"Enter the index of the first element that you want to swap or interchange: "))
index2=int(input(f"Enter the index of the second element that you want to swap or interchange: "))
# In case if you want 1 based indexing.
# index1=index1-1
# index2=index2-1
print(f"After swapping the element at {index1} and {index2} the list is: {Swap(list, index1, index2)}.")