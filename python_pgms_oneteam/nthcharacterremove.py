#removel of nth character from  a string
s=input("enter a string:")
c=int(input("enter a index:"))
l=len(s)
if c>=0 and c<l:
    print(s[:c]+s[c+1:])
else:
    print(s)

        
    
