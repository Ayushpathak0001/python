with open("data.txt","w")as f :
    f.write("Hello \nMy name is Ayush pathak\n")
    f.write("I am learning python\nI am student of Sobhit university\n")
    f.write("I belongs to bihar ")
    
    data=f.write
    print(data)
    
    
with open("demo.txt", "r") as f:
    data = f.read()

new_data = data.replace("python", "java")
print(new_data)

with open("demo.txt", "w") as f:
    f.write(new_data)

    