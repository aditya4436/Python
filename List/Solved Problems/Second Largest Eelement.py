# Time Complexity:- O(n)
# Space Complexity:- O(1)
l=[12, 32, 43, 54, 108]
largest=l[0]
second_largest=0
for i in range(len(l)):
    if(l[i]>largest):
        second_largest=largest
        largest=l[i]

print(second_largest)