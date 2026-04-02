x=int(input("enter your number : "))
fact=1
if x==1 or x==0:
 print(1)
for i in range(2,x+1):
    fact=fact*i
print("factorial of ",x,"is :", fact)
    
