# replace():- Returns a string where a specified value is replaced with
#             a specified value.
string=input("Enter the string: ")
string1=input("Enter the string that you want to replace: ")
string2=input("Enter the string with which you want to replace: ")
print(f"The entered string is: {string}")
print(f"The string which is to be replaced is: {string1}.")
print(f"The string with which the existing string is to be replced is: {string2}.")
print(f"The string after replacing: {string.replace(string1, string2)}.")