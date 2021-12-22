# Create a set
s1 = set()  # empty set
s1.add(1)  # add element to a set
s1.update([2, 3, 4])  # Adds every element of the iterable
s2 = set([2, 4, 6])  # Creates a initialized set
s2.clear()  # Clear the set
s1.discard(3)  # Eliminates 3 from the set
s2.update([2, 4, 3])

print("S1 =", s1)
print("S2 =", s2)
# Unites the sets (creates a set with all non-repeated elements of both sets)
s3 = s1 | s2  # or s3 = s1.union(s2)
# Find the intersection of both sets
s4 = s1 & s2  # or s4 = s1.intersection(s2)
print("S1 ∪ S2 =", s3)
print("S1 ∩ S2 =", s4)
# New set with all elements of the leftside set that arr not in the rightside set
s5 = s1 - s2  # or s1.diference(s2)
# New set with all the elements of both sets that are not in the intersection
s6 = s1 ^ s2
print("S1 - S2 =", s5)
print("S1 - (S1 ∩ S2) =", s6)
