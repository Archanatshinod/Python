n=int(input("enter the no.of names:"))
a=[]
for i in range(n):
    item=input("enter a name:")
    if 'a' in item:
        a.append(item)
print(a)       
    
