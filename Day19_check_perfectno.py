
divisors=[]
n=int(input("Enter a number:"))
for i in range(1,n):
    if n%i==0:
        divisors.append(i)
print(divisors)
perfect=sum(divisors)
# print(perfect)
if perfect==n:
    print(f"{n} is perfect Number")
else:
    print(f"{n} is not a perfect number")




