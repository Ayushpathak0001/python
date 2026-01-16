list =list(input("enter a string : "))
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("not palindrome")
print(type(list))
print(type(copy_list))
