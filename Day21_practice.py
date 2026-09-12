<<<<<<< HEAD
'''
# 1. Print numbers from 1 to 20
for i in range(1,21):
    print(i)

# 2. Print even numbers from 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)

# 3. Find the sum of numbers from 1 to 100
total=0
for i in range(1,101):
    total+=i
print(f"sum={total}")

# 4. Check whether a number is positive, negative or zero
num=int(input("Enter a number"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is zero")

# 5. Print multiplication table
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# 6. Count vowels in a string
count=0
text=input("Enter Text:")
for chr in text:
    if chr.lower() in "aeiou":
        count+=1
print("Number of vowels=",count)

# 7. Reverse a string using a loop
text = input("Enter a string: ")
reverse = ""
for i in text:    
    reverse = i + reverse
print("Reverse =", reverse)

# 8. Check whether a string is palindrome
text=input("Enter String:")
reverse=""
for i in text:    
    reverse = i + reverse
print("Reverse =", reverse)
if reverse==text:
    print("String is palindrome")
else:
    print("String is not a palindrome")
'''
# 9. Find the largest number in a list
numbers=[21,43,75,97,46,46,99,109]
largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
print(f"Largest={largest}")

# 10. Find the smallest number in a list
numbers=[23,45,67,98,46,230,24,34]
smallest=numbers[0]

for num in numbers:
    if num<smallest:
        smallest=num
print(f"Smallest={smallest}")




=======
'''
# 1. Print numbers from 1 to 20
for i in range(1,21):
    print(i)

# 2. Print even numbers from 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)

# 3. Find the sum of numbers from 1 to 100
total=0
for i in range(1,101):
    total+=i
print(f"sum={total}")

# 4. Check whether a number is positive, negative or zero
num=int(input("Enter a number"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is zero")

# 5. Print multiplication table
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# 6. Count vowels in a string
count=0
text=input("Enter Text:")
for chr in text:
    if chr.lower() in "aeiou":
        count+=1
print("Number of vowels=",count)

# 7. Reverse a string using a loop
text = input("Enter a string: ")
reverse = ""
for i in text:    
    reverse = i + reverse
print("Reverse =", reverse)

# 8. Check whether a string is palindrome
text=input("Enter String:")
reverse=""
for i in text:    
    reverse = i + reverse
print("Reverse =", reverse)
if reverse==text:
    print("String is palindrome")
else:
    print("String is not a palindrome")
'''
# 9. Find the largest number in a list
numbers=[21,43,75,97,46,46,99,109]
largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
print(f"Largest={largest}")

# 10. Find the smallest number in a list
numbers=[23,45,67,98,46,230,24,34]
smallest=numbers[0]

for num in numbers:
    if num<smallest:
        smallest=num
print(f"Smallest={smallest}")




>>>>>>> d9ee51f0cc5c114ccd731eff574942c21419d1af
