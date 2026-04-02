import random
win_num=random.randint(1,10)
count=0
while True:
 num=int(input("enter number : "))
 count+=1

 if(win_num>num):
        print("your number is larger")
 elif(win_num<num):
        print("your number is smaller")
 else:
        print("you won")  
 break 
        
     
