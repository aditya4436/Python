list1=[2, 7, 5, 64, 14, 3]
index1=int(input("Enter the index from where you wish to start deleting the elements: "))
index2=int(input("Enter the index upto which you want to delete the elements (The elements just before this index will be deleted): "))
del list1[index1:index2]
print(list1)