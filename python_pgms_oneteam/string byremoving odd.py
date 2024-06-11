#string by removing alphabets at odd positions
s=input("enter a string:")
l=len(s)
new=""
for i in range(0,l):
    if i%2==0:
        new=new+s[i]
print(new)
