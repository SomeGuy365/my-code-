factors = []

number = "a"
while number.isdigit() == False:
    number = input("Enter num:")
number = int(number)

for i in range(1, number+1):
    for b in range(1,number+1):
        if (i*b) == number and i not in factors and b not in factors:
            factors.append(i)
            factors.append(b)

factors.sort()
print(factors)