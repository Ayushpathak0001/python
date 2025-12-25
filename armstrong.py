num = int(input("Enter a number: "))

digits = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
