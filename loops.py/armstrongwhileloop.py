x= input("enter number : ")
sum=0
i=0
while i <len(x):
    sum+=int(x[i])**len(x)
if sum==int(x):
    print("no is armstrong")
else:
    print("no is not armstromg")
i+=1