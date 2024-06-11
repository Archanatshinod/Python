vehicles=[]

def create():
    n=int(input("enter no of vehicles:"))
    
    for i in range(n):
        v=[]
        name=input("enter name of vehicle:")
        v.append(name)
        p=int(input("enter the price:"))
        v.append(p)
        w=int(input("enter the no.of wheels:"))
        v.append(w)
        vehicles.append(v)
        print(vehicles)
def display():
    while True:
        print("1.two wheeler")
        print("2.three wheeler")
        print("3.four wheeler")
        print("3.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            for j in vehicles: 
                if j[2]==2:
                    print(j)

        elif ch==2:
            for j in vehicles:
                    if j[2]==3:
                        print(j)

        elif ch==3:
            for j in vehicles:
                if j[2]==4:
                    print(j)
        elif ch==4:
            break
        else:
            print("invalid!!!")


while True:
    print("1.Add vehicle")
    print("2.Display")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        create()
    elif ch==2:
        display()
    elif ch==3:
        break
    else:
        print("invalid!!!")
    