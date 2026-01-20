nums =[1,2,3,5,6,7,8,9,10]
for el in nums:
    print("\n",el,"\n")

no = [ 1,2,3,4,5,6,7,8,9,10]
for n in no :
    if(n%2==0):
        print("\n",n)

names = ["IRON MAN","HULK","THOR","CAPTAIN AMERICA","WANDA","BLACK WIDOW"]
search =input("enter name to search : ")
i=0

for name in names:
    if name == search:
        print("found",name," AT INDEX ",i)
      
    
    i+=1