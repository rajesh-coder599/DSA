#set
set1={1,2,"rajesh",1,2,100}
print(set1)
print(len(set1))
set1.add("rayal")
set1.add(100)
print(set1)
set1.discard(100)
set1.discard(12)
print(set1)
set2=set1.copy()
print(set2)
set2.clear()
print(set2)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
#union
print(s1|s2)
print(s1.union(s2))
#intersection
print(s1&s2)
print(s1.intersection(s2))
#difference
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))
#symmetric difference
print(s1^s2)
print(s1.symmetric_difference(s2)) # union of s1-s2 & s2-s1 