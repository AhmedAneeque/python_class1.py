''' 
# 11. Count even and odd numbers in a list
numbers=[2,46,34,9,47,34,24,67,1,37,3]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers=",even)
print("Odd numbers=",odd)

# 12. Search for an element in a list
numbers = [ 10, 22, 12, 39, 44, 50]
search = int(input("Enter number to search: "))
found = False
for num in numbers:    
    if num == search:        
        found = True        
        break
if found:    
    print("Number found") 
else:    
    print("Number not found")

# 13. Print only names starting with 'A'
names=["Aneeque","Amit","Rahul","Saadan","Akash","Sameer"]
for name in names:
    if name.startswith("A"):
        print(name)

# 14. Count words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:    
    count += 1
print("Number of words =", count)

# 15. Find the frequency of a character
string = input("Enter a string: ") 
ch = input("Enter character to search: ")
count = 0
for i in string:   
    if i == ch:        
        count += 1
        
print("Frequency =", count)

# 16. Remove duplicate elements from a list
numbers = [10,20,10,30,20,40,30,50,45,76,76]
new_list = []
for num in numbers:    
    if num not in new_list:        
        new_list.append(num)
print("Original list:", numbers) 
print("New list:", new_list)

# 17. Find the second largest number
numbers=[25,67,98,47,43,23,33]
largest=numbers[0]
second=numbers[0]
for num in numbers:
    if num > largest:        
        second = largest        
        largest = num    
    elif num > second and num != largest:        
        second = num
print("Largest =", largest) 
print("Second largest =", second)

# 18. Print prime numbers from 1 to 100
for num in range(2, 101):   
    prime = True
    for i in range(2, num):       
        if num % i == 0:            
            prime = False            
            break
    if prime:        
        print(num)

# 19. Separate positive and negative numbers
numbers = [12,-5,25,-8,15,-2,30,50,76]
positive = [] 
negative = []
for num in numbers:    
    if num >= 0:        
        positive.append(num)    
    else:        
        negative.append(num)
print("Positive:", positive) 
print("Negative:", negative)
'''
# 20. Student marks and grade
marks = [76,55,87,92,75]
total = 0
for mark in marks:
    total += mark

percentage = total / len(marks)
print("Total =", total) 
print("Percentage =", percentage)

if percentage >= 90:    
    print("Grade A+") 
elif percentage >= 80:    
    print("Grade A") 
elif percentage >= 70:    
    print("Grade B") 
elif percentage >= 60:    
    print("Grade C") 
elif percentage >= 40:    
    print("Grade D") 
else:    
    print("Fail")