num1=float(input("enter your first number : "))
num2=float(input("enetr your second number : "))
print("select your operation")
print("click 1 for addition")
print("click 2 for substraction")
print("click 3 for multiplication")
print("click 4 for divison")

choice=int(input("enter your choice : "))

if choice ==1:
    print("your addition is : ",num1+num2)
elif choice ==2:
    print("your substraction is : ",num1-num2)
elif choice == 3:
    print("your multiplication is : ",num1*num2)
elif choice==4:
    print("your divison is ",num1/num2)
else:
    print("invalid choice")
    