num=int(101)
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("It is a palindrome")
    print (hex(num))
else:
    print("Not a palindrome!")
