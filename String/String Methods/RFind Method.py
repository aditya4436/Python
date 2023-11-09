# rfind():- This method is finds the last occurrence of the specified value.
#           The rfind() method returns -1 if the value is not found.
#           The  rfind() method method is almost the same as rindex() method.
string=input("Enter the string: ")
string1=input("Enter the string which you want to find: ")
print(f"The string is: {string}")
print(f"The string which is to be searched: {string1}")
print(f"The string starts from the index: {string.rfind(string1)}.")