# maketrans():- This method returns a mapping table that can be used with
#               the translate(), method to replace specified characters.
string=input("Enter a string: ")
char=input("Enter the character that you want to replace: ")
char1=input("Enter the character with which you want to replace: ")
mystring=string.maketrans(char, char1)
print(f"The string after transplantation: {string.translate(mystring)}.")