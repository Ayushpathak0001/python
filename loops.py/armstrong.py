x=input("enter number to check armstrong : ")
sum=0
for i in range(len(x)):
    sum+=int(x[i])**len(x)
if sum == int(x):
     print("no is armstrong")
else:
     print("no is not armstrong")
    
    