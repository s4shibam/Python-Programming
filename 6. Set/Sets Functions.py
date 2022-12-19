s1 = set([2, 5, 6, 7, 9, 12, 20, 25, 60])
s2 = set([1, 3, 4, 8, 9, 15, 12, 20])
s3 = set([11, 17, 19, 21])

print("s1 = ", s1)
print("Length of s1 = ", len(s1))
print("Minimum value in s1 = ", min(s1))
print("Maximum value in s1 = ", max(s1))

print("\ns2 = ", s2)
print("Length of s2 = ", len(s2))
print("Minimum value in s2 = ", min(s2))
print("Maximum value in s2 = ", max(s2))

print("\ns3 = ", s3)
print("Length of s3 = ", len(s3))
print("Minimum value in s3 = ", min(s3))
print("Maximum value in s3 = ", max(s3))

su = s1.union(s2)  # Union of Set
# su = s1 & s2
print("\nUnion of Set s1 & s2 = ", su)

si = s1.intersection(s2)  # Intersection of Set
print("Intersection of Set s1 & s2 = ", si)

print("\ns1 & s3 are Disjoint Sets? = ", s1.isdisjoint(s3))

s3.remove(11)
print("\nNew s3 = ", s3)
