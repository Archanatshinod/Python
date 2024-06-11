n=int(input("enter the limit:"))
sum=0
for i in range(1,n):
    if i%2==0:
        continue
    else:
        sum=sum+i
print("sum of odd numbers:",sum)
