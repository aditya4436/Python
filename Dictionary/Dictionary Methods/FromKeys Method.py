# fromkeys():- Returns a dictionary with the specified keys and value.
# Note:- fromkeys() takes two argument, i.e., key and value, value is
# optional but we must pass the key which will create a new dictionary.
# and by default the value of the keys are 'None' by default.
dictionary={1: "Aditya", 2: "Kumar",  3: "Pawan"}
print("The old existing dictionary is: ", dictionary)
string=input("Enter any iterable object from the given dictionary to  create a new dictionary out of it: ")
print("The newly created dictionary is: ", dict.fromkeys(string))