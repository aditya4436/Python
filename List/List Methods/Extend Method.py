# extend():- Adds each element of the iterable object to the end
#            of the list.
list1=[2, 4, 6, 8, 10]
list2=[1, 3, 5, 7, 9]
print("Before extending the lists: ")
print("list1: ",list1)
print("list2: ",list2)
list1.extend(list2)
print("After extending the list1 with list2: ", list1)