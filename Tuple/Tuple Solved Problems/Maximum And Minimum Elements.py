# Time Complexity:- O(n)
# Space Complexity:- O(1)
def MaximumAndMinimum(tup, maximum, minimum):
    for i in range(len(tup)):
        if maximum<tup[i]:
            maximum=tup[i]
        if minimum>tup[i]:
            minimum=tup[i]
    print(f"The maximmum element is: {maximum}")
    print(f"The minimum element is: {minimum}")

tup=(3, 7, -1, 108, 1, 18, 9)
maximum=tup[0]
minimum=tup[0]        
MaximumAndMinimum(tup, maximum, minimum)