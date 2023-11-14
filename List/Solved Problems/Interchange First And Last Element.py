list=[2, 11, 20, 29]
temp=list[0]
list[0]=list[len(list)-1]
list[len(list)-1]=temp
print(f"After swapping the first and the last element the list is: {list}")