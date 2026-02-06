with open("data.txt","w")as f :
    f.write("Hello \nMy name is Ayush pathak\n")
    f.write("I am learning python\nI am student of Sobhit university\n")
    f.write("I belongs to bihar \n \n")
    
with open("data.txt","r") as f:
    data=f.read()
    print(data)
    
new_data=data.replace("Ayush","Shivam")

with open("data.txt","w") as f:
    f.write(new_data)

print(new_data)
