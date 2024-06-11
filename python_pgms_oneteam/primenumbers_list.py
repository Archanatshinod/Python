n=int(input("enter the limit:"))
prime=[]
for i in range(n):
    item=int(input("enter a number:"))
    for i in range(2,n):
        if item%i==0:
            break
    else:
        prime.append(item)
            
print(prime)
