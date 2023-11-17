# Time Complexity:- O(n)
# Space Complexity:- O(1)
list1=[2, 7, 5, 64, 14, 3]
odd=0
even=0
for i in range(len(list1)):
    if list1[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print(f"There are {odd} odd numbers in the list.")
print(f"There are {even} even numbers in the list.")