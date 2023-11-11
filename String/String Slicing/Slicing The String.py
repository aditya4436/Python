# Taking index as input from the user.
string=input("Enter any string: ")
print(f"The length of the string is: {len(string)}")
n1=int(input("Enter the index from where you want to slice the string: "))
n2=int(input("Enter the index upto which you want to slice the string: "))
print(f"It will print the string from index {n1} to {n2-1}.")
print(f"After the slicing the string: {string[n1:n2]}.")
