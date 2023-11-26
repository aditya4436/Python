from sys import maxsize
minimum_int=-(maxsize)
def SecondLargest(arr):
    largest=arr[0]
    second_largest=minimum_int
    for i in range(0, len(arr)):
        if largest<arr[i]:
            second_largest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest

l=[10, 25, -12, -6, 20, 20]
print(SecondLargest(l))