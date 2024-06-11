#### sorting a list ####
n=int(input("enter the number of elements:"))
number=[]
for i in range(n):
    a=int(input("enter the number:"))
    number.append(a)

for i in range(0,n):
    for j in range(i+1,n):
        if number[i]<number[j]:
            temp=number[i]
            number[i]=number[j]
            number[j]=temp

for j in range(0,n):
    print(number[j])


###odd numbers from a list ###

n=int(input("enter the number of elements:"))
number=[]
sum=0
for i in range(n):
     a=int(input("enter the number:"))
     number.append(a)
for j in number:
     if j%2==0:
          continue
     else:
          sum=sum+j
print("sum of odd nos in this list:",sum) 

### primenumbers from a range ####
a=int(input("enter the starting number:"))
b=int(input("enter the ending number:"))
f=0
for i in range(a,b):
    n=int(i/2)
    for j in range(2,n):
        if i%j==0:
            f=1
            break
    
    if f==0:
        print(i)
    







##vowels in a given string ####
count=0
v=['a','e','i','o','u']
str=input("enter the string:")
print("the vowels in given string:")
for i in str:
    if i in v:
        count=count+1
        print(i)
print("no.of. vowels:",count)

      