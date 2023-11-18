# Time Complexity:- O(n)
# Space Complexity:- O(1)
tup1=([2, 11], [20, 29])
x=2
# result=[tuple(i*x for i in sub) for sub in tup1]
# print(f"The updated list is: {result}")

result=[tuple(map(lambda element: element*x, sub)) for sub in tup1]
print(f"The updated list is: {result}")