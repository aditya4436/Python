# Time Complexity:- O(n)
# Space Complexity:- O(1)
def Summation(tup):
    sum=0
    for i in range(len(tup)):
        sum+=tup[i]
    return sum

test_tup=(7, 8, 9, 1, 7, 10)
print(f"The sum of the elements in the tuple is: {Summation(test_tup)}")

# List Comprehension
# test_tup=(7, 8, 9, 1, 7, 10)
# result=[i for i in test_tup ]
# print(sum(result))