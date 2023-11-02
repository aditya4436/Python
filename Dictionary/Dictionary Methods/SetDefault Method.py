# setdefault():- Returns the value of the specified key. If the key does not
#                exist: insert the key, with the specified value.
dictionary={1: "Data", 2: "Structure", 3: "And", 4: "Algorithm"}
n=int(input("Enter the key to access or print the value or add the value: "))
print(f"The data at key {n} is {dictionary.setdefault(n)}")
print(f"If the key does not exist the entered key is added to the dictionary: {dictionary}")