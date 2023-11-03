# center():- Returns a centered string.
string=input("Enter any string: ")
# print("The string is: ", string)
n=int(input("Enter the number of whitespaces you want before the string: "))
print(f"{string.center(n)}")