<<<<<<< HEAD
#check for prime numbers 
# primes=[]
# for n in range(int(input("enter starting Number:")),int(input("Enter last number:"))):
#     if n==1:
#         pass
#     else:
#         for d in range(2,(n//2)+1):
#             if n%d==0:
#                 break
#         else:
#             primes.append(n)
# print(f"{primes}\n are prime Numbers")

#check prime number
n=int(input("Enter number"))
for d in range(2,(n//2)+1):
    if n%d==0:
        print("number is not prime:")
        break
        
    
else:
    print("number is prime")
=======
#check for prime numbers 
# primes=[]
# for n in range(int(input("enter starting Number:")),int(input("Enter last number:"))):
#     if n==1:
#         pass
#     else:
#         for d in range(2,(n//2)+1):
#             if n%d==0:
#                 break
#         else:
#             primes.append(n)
# print(f"{primes}\n are prime Numbers")

#check prime number
n=int(input("Enter number"))
for d in range(2,(n//2)+1):
    if n%d==0:
        print("number is not prime:")
        break
        
    
else:
    print("number is prime")
>>>>>>> d9ee51f0cc5c114ccd731eff574942c21419d1af
