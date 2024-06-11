l=int(input("enter the n1:"))
t=int(input("enter the n2:"))
for i in range(1,l+1):
    if l%i==0:
        if t%i==0:
            gcd=i
print("gcd:",gcd)
