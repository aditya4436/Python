# Time Complexity:- O(n)
# Space Complexity:- O(1)
arr=[1, 2, 3, 8, 4, 9, 12]
sum=0
for i in range(0, len(arr)):
    sum+=arr[i]
print(f"The sum of the elements in the list is: {sum}")