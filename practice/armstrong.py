x=input("enter your number : ")
sum=0
for i in range(len(x)):
    sum+=int(x[i])**len(x)
    
if sum==int(x):
    print("The no",x,"is Armstrong ")
else:
    print("The no",x,"is not Armstrong ")