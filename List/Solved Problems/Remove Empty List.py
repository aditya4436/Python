# Time Complexity:- O(n)
# Space Complexity:- O(n)
list1=[2, [], 7, 5, [], 64, 14, [], 3]
list2=[element for element in list1 if element != []]
print(f"Before removing the empty list from the list: {list1}")
print(f"After removing the empty list from the list: {list2}")

# Time Complexity:- O(n)
# Space Complexoty:- O(1)
# list2=list(filter(None, list1))
# print(list2)