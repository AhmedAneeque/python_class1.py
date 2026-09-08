perfect_numbers = []

for n in range(int(input("enter starting Number:")),int(input("Enter last number:"))+1):
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    perfect = sum(divisors)

    if perfect == n:
        print(f"{n} is a perfect number")
        perfect_numbers.append(n)
    # else:
    #     print(f"{n} is not a perfect number")
    #     pass

print(perfect_numbers)
print("these are perfect numbers")
