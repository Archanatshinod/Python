l=int(input("enter the number:"))
temp=l
rev=0
sum=0
while(temp>0):
    d=temp%10
    temp=int(temp/10)
    rev=(rev*10)+d

print(rev)
if l==rev:
    print("palindrome")
else:
    print("not palindrome")
