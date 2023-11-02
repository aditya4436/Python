# get():- Returns the value of the specified key.
dictionary={1: "Software", 2: "Development", 3: "Competitive", 4: "Programming"}
n=int(input("Enter the key to access its value: "))
print(f"The value at key {n} is: {dictionary.get(n)}")