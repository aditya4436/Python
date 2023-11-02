# pop():- Removes element with the specified key.
dictionary={1: "Software", 2: "Development", 3: "Competitive", 4: "Programming"}
print(f"The items in the dictionary are: {dictionary}")
n=int(input("Enter the key whose value you want to pop out: "))
dictionary.pop(n)
print(f"The dictionary after poping out the specified value: {dictionary}")