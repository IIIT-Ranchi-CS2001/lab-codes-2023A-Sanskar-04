n = int(input("Enter a number:"))
total = 0
print("The number is ", n)
while n > 0:
    digits = n % 10
    total = total + digits
    n = n // 10

print("The total sum of digits is:", total)
