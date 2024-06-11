students=[]

def create():
    n=int(input("enter no of students:"))
    for i in range(n):
        student={}
        name=input("enter name of student:")
        for i in students:
            if name in i['name']:
                print("name does not exist")
        else:
            stud={}
            for j in ['maths','english','science']:
                m=int(input(f"enter {j} score  {name}"))
                stud[j]=m
                
            student['name']=name
            student['marks']=stud
            students.append(student)
        print(students)




def display():
    def mathss(a):
        for k in students:
            print(f"{k['name']},{k['marks'][a]}")
    while True:
        print("1.maths score")
        print("2.english score")
        print("3.science score")
        print("3.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            mathss('maths')

        elif ch==2:
            mathss('english')

        elif ch==3:
            mathss('science')
        elif ch==4:
            break
        else:
            print("invalid!!!")

while True:
    print("1.create student")
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
    

