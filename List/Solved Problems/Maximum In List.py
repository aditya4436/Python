# Time Complexity:- O(n)
# Space Complexity:- O(1)
list=[1, 2, 3, 8, 4, 9, 12]
# print(f"The largest element in the list is: {max(list)}.")
m=0
for i in range(0, len(list)):
    if list[i]>m:
        m=list[i]

print(f"The maximum element is: {m}.")