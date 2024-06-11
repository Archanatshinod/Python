stud={}
l=[]
def create(n):
    for i in range(n):
        id=input("enter the roll no :")
        name=input("enter the name of the student:")
        stud[id]=name
        l.append(stud)

def edit():
    id=input("enter the roll no :")
    if id in stud:
        newname=input("enter the new name:")
        stud[id]=newname
    else:
        print("invalid!!!")
    
def delete():
    if id in stud:
        id=input("enter the roll no :")
        del stud[id]
    else:
        print("invalid!!!")
def display():
    id=input("enter the roll no :")
    if id in stud:
        print("Name:",stud[id])
    else:
        print("invalid!!!")



while True:
    print("1.create")
    print("2.edit")
    print("3.delete")
    print("4.Display")
    print("5.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        n=int(input("enter the number of students: "))
        create(n)
    elif ch==2:
        edit()
    elif ch==3:
        delete()
    elif ch==4:
        display()
    elif ch==5:
        break
    else:
        print("invalid!!!")


    


