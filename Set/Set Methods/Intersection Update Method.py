# intersection_update():- Removes the items in this set that are not present
#                         in other, specified set(s).
set1={34, 21, 54, 90, 78}
set2={33, 21, 24, 90, 108}
print(f"The first set is: {set1}")
print(f"The second set is: {set2}")
set1.intersection_update(set2)
print(f"The updated set1 with the intersection of the two set is: {set1}")