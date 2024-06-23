def add(*x):
    sum=0
    for i in x:
        sum+=i
    return sum
n1=int(input("first number:"))
n2=int(input("second number:"))
sum1=add(n1,n2)
print(sum1)
n3=7
n4=8
n5=6
sum2=add(n1,n2,n3)
print(sum2)
sum3=add(n1,n2,n4)
print(sum3)
sum4=add(n1,n2,n3,n5,n4)
print(sum4)
