##################################################################### OOPS CONCEPTS IN PYTHON #############################################################################################
##### Class #######
class employee:
    id=10
    name="devnash"
    def display(self):
        print(self.id,self.name)
##### Object #####
obj1=employee()
obj1.display()

class employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print("ID:%d \n Name:%s"%(self.id,self.name))

emp1=employee("john",101)
emp2=employee("david",102)

emp1.display()
emp2.display()

#constructor-non parameterized

class student:
    def __init__(self):
        print("this is non parameterized")
    def show(self,name):
        print("hello",name)
Student=student()
Student.show("john")
        
### built-in functions

class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s=Student("archana",100,21)
print(getattr(s,'name'))
setattr(s,"age",23)
print(getattr(s,'age'))
print(hasattr(s,'id'))
delattr(s,'age')
print(s.age)



##### inheritance #####

#single
class animal:
    def speak(self):
        print("Animal speaking")
class dog(animal):
    def bark(self):
        print("dog barking")
d=dog()
d.bark()
d.speak()


#multilevel

class animal:
    def speak(self):
        print("Animal speaking")
class dog(animal):
    def bark(self):
        print("dog barking")
class dogchild(dog):
    def eat(self):
        print("eating bread")
d=dogchild()
d.bark()
d.speak()
d.eat()

#multiple

class cal1:
    def sum(self,a,b):
        return a+b
class cal2:
    def mul(self,a,b):
        return a*b
class derived(cal1,cal2):
    def divide(self,a,b):
        return a/b
d=derived()
print(d.sum(10,20))
print(d.mul(10,20))
print(d.divide(10,20))

#hierarchical

class parent:
    def func1(self):
        print("this is parent")
class child1(parent):
    def func2(self):
        print("this is child1")      

class child2(parent):
    def func3(self):
        print("this is child2")    

obj1=child1()
obj2=child2()
obj1.func1() 
obj1.func2() 
obj2.func1() 
obj2.func3()

##### polymorphism #####

class bird:
    def intro(self):
        print("thre are many types of birds")
    def flight(self):
        print("most of birds can fly some cannot")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostriches can not fly")

obj_bird=bird()
obj_spr=sparrow()
obj_ost=ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()

class base:
    def e(self):
        self.a="hello"
        self.__c="world"
        print(self.__c)
class derived(base):
    def d(self):
        print("calling private member ")
        # base.__init__(self)
        # print(self.__c)
obj1=base()
obj2=derived()
print(obj1.__c)
obj2.e()

## question
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def carea(self):
        area=self.length*self.width
        print("area of rectangle:",area)

l=int(input("enter length:"))
w=int(input("enter width:"))
obj=rectangle(l,w)
obj.carea()