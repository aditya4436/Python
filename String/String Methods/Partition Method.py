# partition():- Returns a tuple where the string is parted into three parts.
string=input("Enter the string: ")
print(f"The entered string is: {string}.")
string1=input("Enter the string that you want to partition: ")
print(f"The string to be partitioned is: {string1}")
print(f"The string after partitioning: {string.partition(string1)}")