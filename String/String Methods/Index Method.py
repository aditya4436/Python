# index():- Returns the index of the first occurence of the specified character
#           or value.
string=input("Enter a string: ")
print(f"The string is: {string}.")
char=input("Enter the character whose index you want to print or see: ")
print(f"The entered character is at index number: {string.index(char)}")