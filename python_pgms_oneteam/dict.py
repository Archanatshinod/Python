d={}
n=int(input("enter the no.of items:"))
for i in range(n):
    d1=input("enter the keys:")
    if d1 in d:
        print("key already exist!!!")
        break
    else:
        d2=input("enter the values:")
    d[d1]=d2
print(d)
        
        
      
