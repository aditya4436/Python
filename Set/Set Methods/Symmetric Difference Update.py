# symmetric_difference_update():- Inserts the symmetric differences from this set and another.
#                                 Basically it updates one set(set1) with the symmetric difference
#                                 of two sets(set1 and set2).
set1={11, 18, 2, 108}
set2={11, 108, 21, 34}
print(f"The first set is: {set1}")
print(f"The second set is: {set2}")
set1.symmetric_difference_update(set2)
print(f"The updated set1 with the symmetric difference is: {set1}")