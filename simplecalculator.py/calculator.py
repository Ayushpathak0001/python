num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nEnter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition is:", num1 + num2)

elif choice == 2:
    print("Subtraction is:", num1 - num2)

elif choice == 3:
    print("Multiplication is:", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Division is:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")
