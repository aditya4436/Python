# startswith():- Returns true if the string starts with the specified value.
string=input("Enter the string: ")
char=input("Enter the character to check if it starts with it or not: ")
print("The entered string is: ", string)
print(f"The string starts with {char}: {string.startswith(char)}")