s1={40,54,86,95,300}
s2={50,500,57,43,300}

s1.clear()
print(s1)

s2.discard(57)
print(s2)

s2.add(30)
print(s2)

s3=s1.isdisjoint(s2)
print(s3)

s2.pop()
print(s2)

del(s3)           #function

s2.remove(43)
print(s2)

s2.update(s1)
print(s2)

s4=s1.symmetric_difference(s2)
print(s4)

s5=s2.copy()
print(s5)