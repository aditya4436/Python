# symmetric_difference():- Returns a set with the symmetric differences from
#                          this set and another. Basically it returns the items
#                          which are not common between two sets.
set1={11, 18, 2, 108}
set2={11, 108, 21, 34}
print(f"The first set is: {set1}")
print(f"The second set is: {set2}")
print(f"The set after removing an element: {set1.symmetric_difference(set2)}")