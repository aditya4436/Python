# Time Complexity:- O(n)
# Space Complexity:- O(1)
arr=[1, 2, 3, 8, 4, 9, -12]
minElement=max(arr)
for i in range(0, len(arr)):
    if minElement>arr[i]:
        minElement=arr[i]

print(f"The minimum element in the list is: {minElement}.")