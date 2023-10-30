# remove():- Removes a given object from the list. It does not returns anything.
list=[21, 32, 43, 54]
print(f"Before removing an element from the list: {list}.")
element=int(input("Enter the element to remove from the list: "))
list.remove(element)
print(f"After removing the given element from the list: {list}")