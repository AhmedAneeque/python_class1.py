#Read marks in 3 subjects phy,chem and bio of a student

phy=int(input("Enter marks of physics:"))
chem=int(input("Enter marks of Chemisty:"))
bio=int(input("Enter marks of Biology:"))
total=phy+chem+bio
print(f"Total={total}")

if total>=550 :
    print("You are elligible for MBBS")
elif total<550 and total>=450:
    print("You are elligible for BDS")
elif total<450 and total>=350:
    print("You are elligible for BUMS")
elif total<350 and total>=200:
    print("You are elligible for BAMS")
else:
    print("You are not elligible")

#calculate electricity bill amount

units=int(input("Enter number of units:"))
if units<=200:
    amount=units*5
elif units>200 and units<=300:
    amount=1000+(units-200)*6
elif units>300 and units<=400:
    amount=1600+(units-300)*7
elif units>400 and units<=500:
    amount=2300+(units-400)*8
else:
    amount=3100+(units-500)*10

print(f"total bill amount={amount}")

