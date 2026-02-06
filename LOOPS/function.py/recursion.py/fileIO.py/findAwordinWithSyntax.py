with open("practice.txt","w") as f:
    f.write("My Name is Ayush Pathak\nI am from Bihar,India\n")
    f.write("I am pursiung BCA from Sobhit Univeristy Meerut\nI am in section B\n")
    f.write("I Want to become a Engineer in future\n")
    f.write("I want to start my own buisness in future\n \n")
    
    
with open("practice.txt","r")as f:
        data=f.read()
        print(data)
       
        
    
new_data=data.replace("Ayush","RAJ")

with open("practice.txt","w") as f:
    f.write(new_data)

print(new_data)


with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("Sobhit")!=-1):
        
        print("found")
    else:
        print("not found")
        
        

    
