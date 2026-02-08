count=0
with open("numbers.txt","w") as f:
    f.write("1,2,4,6,5,64,24,75,84,24,101,435\n")
    
with open("numbers.txt","r")as f:
    data=f.read()
    print(data)
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            print(val)
            count+=1
    
    print(count)