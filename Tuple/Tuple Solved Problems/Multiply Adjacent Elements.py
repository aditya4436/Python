# Time Complexity:- O(n)
# Space Complexity:- O(n)
tup1=(1, 5, 7, 8, 10)
# result=tuple(i*j for i, j in zip(tup1, tup1[1:]))
# print(result)

result=tuple(map(lambda i, j: i*j, tup1[1:], tup1[:-1]))
print(f"The result is: {result}.")
