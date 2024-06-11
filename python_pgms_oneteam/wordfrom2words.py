#new string created by concatinating 2 user input strings seperated by space and swapping first character of that two strings
s=input("enter a string1:")
c=input("enter a string2:")
a=c[:2]+s[2:]
b=s[:2]+c[2:]
print(a+" "+b)
