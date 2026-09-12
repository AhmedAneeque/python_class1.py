list=[12,34,65,78,45,76,56,34,67]
print(list)

list.append(24)
print(list)

list.insert(2,15)
print(list)

i=list.index(34)
print(i)

c=list.count(34)
print(c)

list.sort()
print(list)
print(list[ : :-1])
'''
list.reverse()
print(list)
'''
list2=["Apple","Mango","orange"]
list.extend(list2)
print(list)

list.pop()
print(list)

list.remove(67)
print(list)

#shallow copy
'''
list3=list
print(list)
print(list3)
'''
#deep copy
list3=list.copy()
print(list3)
