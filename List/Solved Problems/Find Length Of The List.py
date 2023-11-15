# Time Complexity:- O(n)
# Space Complexity:- O(1)
list=[1, 2, 3, 8, 4, 9]
count=0
for i in list:
    count=count+1
print(f"There are {count} elements in the list.")

# from operator import length_hint
# list=[1, 2, 3, 8, 4, 9]
# print(length_hint(list))