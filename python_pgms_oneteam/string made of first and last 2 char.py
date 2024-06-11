# new string made from first and last two character of a string
s=input("enter a string:")
l=len(s)
if l<=4:
    print(s)
else:
    print(s[:2]+s[-2:])
