n=int(input("enter the no.of names:"))
names=[]
e=[]
for i in range(n):
    item=input("enter a name:")
    names.append(item)
print("list of names:",names)
for i in names:
    if 'e' in i:
        e.append(i)
print("names having e:",e)     
