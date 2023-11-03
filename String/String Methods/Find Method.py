# find():- Searches the string for specified character or value and returns
#          the position of where it was found.
string=input("Enter any string: ")
print("The string is: ", string)
char=input("Enter the character whose index you want to return: ")
print(f"The character occurs at index: {string.find(char)}")