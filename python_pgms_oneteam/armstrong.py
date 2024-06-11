l = int(input("Enter the lower range: "))
u = int(input("Enter the upper range: "))
a = len(str(l))  
for i in range(l, u + 1):
    temp = i
    sum = 0
    while temp > 0:
        n = temp % 10
        rev = n ** a  
        sum += rev
        temp //= 10  
    if sum == i:  
        print(i)

 
