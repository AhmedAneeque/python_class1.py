basket1={"mango","banana","orange","apple"}
basket2={"mango","banana","water melon","pineapple"}
print(basket1)
print(basket2)

basket1.update(basket2)
print(basket1)

basket=basket1.union(basket2)
print(basket)

basket3=basket1.intersection(basket2)
print(basket3)

basket1.intersection_update(basket2)
print(basket1)

basket1.difference(basket2)
print(basket1)

basket4=basket1.difference_update(basket2)
print(basket4)


