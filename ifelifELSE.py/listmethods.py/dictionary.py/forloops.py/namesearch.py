names = ["AYUSH","AMAN","ARNAV","ANUSHKA","KANISHKA","AYUSH"]
search =input("enter name to search : ")
i=0


for name in names:
    if name == search:
        print("found",name," AT INDEX ",i)
      
    
    i+=1
    