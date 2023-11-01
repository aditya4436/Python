# discard():- Removes the specified item or element.
set={1, 2, 3, 4, 5}
print(f"Before discarding an element from the set: {set}")
n=int(input("Enter the element that you want to discard: "))
set.discard(n)
print(set)