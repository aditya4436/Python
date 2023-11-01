# difference(): Returns a set containing the difference of two
#               or more sets. Or it prints the unique element
#               which is present in either of the set but not 
#               in both the set.
set1={1, 2, 3, 4, 5}
print(f"The first set is: {set1}")
set2={9, 1, 2, 4, 7, 6, 5, 8, 3}
print(f"The second set is: {set2}")
print(f"The difference of two set: {set2.difference(set1)}")