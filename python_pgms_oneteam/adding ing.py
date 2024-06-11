s=input("enter a string:")
l=len(s)
if l>3:
    if 'ing' in s:
        print(s+'ly')
    else:
        print(s+'ing')
else:
    print(s)
