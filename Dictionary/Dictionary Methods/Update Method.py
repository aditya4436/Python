# update():- Updates the dictionary with the specified key-value pairs.
dictionary={1: "Data", 2: "Structure", 3: "And", 4: "Algorithm"}
print("The dictionary before updating: ", dictionary)
n=int(input("Enter the key for the value that you want to update dictionary with: "))
string=input("Enter the value with which you want to update the dictionary: ")
dictionary.update({n: string})
print("The dictionary after updating: ", dictionary)