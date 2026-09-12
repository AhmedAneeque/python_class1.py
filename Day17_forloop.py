#1: Display numbers from 1 to 10 by using for loop
# for i in range(1,11):
#     print(i)

#2: Display all odd numbers in the range given by user
# for i in range(int(input("Enter first number:")),int(input("Enter second number:"))+1):
#     if i%2==1:
#         print(i)

# 3: Display all numbers which are divisible by n in the range given by the user
f,l=map(int,input("Enter first and last number").split())
n=int(input("Enter the number"))
if n>l:
    print(f"Enter the number less than {l} ")
else:
    for i in range(f,l):
        if i%n==0:
            print(i)