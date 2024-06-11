n=int(input("enter the no.of items:"))
l=[]
for i in range(n):
    item=input("enter a names:")
    l.append(item)
l2 = []
for item in l:
    if item not in l2:
        l2.append(item)
print(l2)
    
