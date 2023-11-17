# Time Complexity:- O(n)
# Space Complexity:- O(1)
import sys
tup=("A", 1, "B", 2, "C", 3)
# This will print the number of elements in tuple.
# count=0
# for i in tup:
#     count=count+1
# print(count)

# This will print the memory occupied by the tuple.
print("Using getsizeof() function.")
print(f"The memory occupied the tuple is {str(sys.getsizeof(tup))} bytes.")
print("\nUsing __sizeof__() function.")
print(f"The memory occupied the tuple is {tup.__sizeof__()} bytes.")