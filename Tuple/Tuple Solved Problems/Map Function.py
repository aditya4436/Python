# Time Complexity:- O(n)
# Space Complexity:- O(n)
def Summation(test_tup):
    sum=0
    for i in range(len(test_tup)):
        sum+=test_tup[i]
    return sum

tup=([2, 11], [20, 29])
result=sum(map(Summation, tup))
print(f"The sum of the elements of the tuple of the list: {result}")