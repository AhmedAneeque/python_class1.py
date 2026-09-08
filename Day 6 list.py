#Collection List
fruits=["apple","banana","pineapple","orange","kivi"]
print(fruits)
print(fruits[1])
fruits[1]="watermelon"
print(fruits[1])
fruits.append("orange")
print(fruits)
print(fruits[-2])
print(type(fruits))
print(type(fruits[1]))

#slicing
print(fruits[:])
print(fruits[1:3])
print(fruits[:3])
print(fruits[1:])

#nested List
orders=["mouse","keyboard","CPU",["orange","watermelon","apple"],[100,56,85],[True,False]]
print(orders)
print(orders[3])
print(orders[3][1])
print(type(orders[4][1]))
