n=int(input("Enter a number : "))
if n>1:
    for i in range (2,n):
        if n % i==0:
            print("Not prime number ")
            break
        else:
            print("Prime number")
            break

else:
                print("Not prime number")
