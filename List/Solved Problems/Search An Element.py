arr=[1, 2, 3, 8, 4, 9, 12]
n=12
# LINEAR SEARCH
# Time Complexity:- O(n)
# Space Complexity:- O(1)
# flag=False
# for i in range(len(arr)):
#     if arr[i]==n:
#         flag=True
#     else:
#         flag=False

# if(flag==True):
#     print("Exists")
# else:
#     print("Does not exist.")
if n in arr:
    print(f"The element exists at index {arr.index(n)}")
else:
    print("Does not exists.")