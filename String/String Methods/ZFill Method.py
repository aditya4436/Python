# zfill():- This method adds zeros(0) at the beginning of the string, 
#           untill it reaches the specified length.
string=input("Enter the string: ")
print(f"The string is: {string}")
n=int(input("Enter the length: "))
print(f"The string after adding 0 at the beginning of string until it reaches the specified value{string.zfill(n)}")