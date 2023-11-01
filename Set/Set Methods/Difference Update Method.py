set1={1, 2, 3, 4, 5}
print(f"The first set is: {set1}")
set2={9, 1, 2, 4, 7, 6, 5, 8, 3}
print(f"The second set is: {set2}")
set2.difference_update(set1)
print(f"The set2 is updated with the difference of the two sets :{set2}")