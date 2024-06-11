n=int(input("enter the no.of items:"))
l=[]
for i in range(n):
    item=int(input("enter a number:"))
    l.append(item)
l.sort()
print("second smallest number:",l[2])
