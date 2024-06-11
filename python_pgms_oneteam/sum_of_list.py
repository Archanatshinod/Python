n=int(input("enter the no.of items:"))
l=[]
for i in range(n):
    item=int(input("enter a number:"))
    l.append(item)
sum=0
for i in l:
    sum=sum+i
print(sum)
