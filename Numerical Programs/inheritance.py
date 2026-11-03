class Parent:
    def __init__(self):
        self.a=10
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=20
c1=Child()
print(c1.b)
print(c1.a)
print("============")
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=20
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c=30
c1=C()
print(c1.a)
print(c1.b)
print(c1.c)
print("============")
print("with out inheritance")
class CargoPlane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry(self):
        print("plane carry cargo")
class PassengerPlane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry_p(self):
        print("plane carry passenger")
class FighterPlane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry_w(self):
        print("plane carry weapons ")
c=CargoPlane()
p=PassengerPlane()
f=FighterPlane()
c.takeoff()
c.land()
c.carry()
c.fly()
p.takeoff()
p.land()
p.fly()
p.carry_p()
f.takeoff()
f.land()
f.fly()
f.carry_w()
print("====================")
class Plane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
class CarGo(Plane):
    def carry(self):
        print("plane carry cargo")
class PassengerPlane(Plane):
    def carry_p(self): 
        print("plane carry passenger")
class FighterPlane(Plane):
    def carry_w(self):
        print("plane carry weapons ")
c=CarGo()
p=PassengerPlane()
f=FighterPlane()
c.takeoff()
c.land()
c.carry()
c.fly()
p.takeoff()
p.land()
p.fly()
p.carry_p()
f.takeoff()
f.land()
f.fly()
f.carry_w()  
print("================================")
class Animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def walk(self):
        print("animal is walking")
class Dog(Animal):
    def bark(self):
        print("dog is barking")
class Tiger(Animal):
    pass
class Monkey(Animal):
    pass
Dog()
d=Dog()
t=Tiger()
m=Monkey()
t.eat()
t.sleep()
t.walk()
d.bark()
d.eat()
d.sleep()
d.walk()
m.eat()
m.sleep()
m.walk()
Tiger()
print("====================")
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        A.dispA(self)
        print("B")
        A.dispA(self)
b=B()
b.dispA()
b.dispB()
print("====================")
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
        
class C(B):
    def dispC(self):
        print("c")
c=C()
c.dispA()
c.dispB()
c.dispC()
print("====================")
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
        
class C(A):
    def dispC(self):
        print("c")
c=C()
b=B()
c.dispA()
c.dispC()
b.dispA()
b.dispB()
print("====================")
class A:
    def dispA(self):
        print("A")
class B:
    def dispB(self):
        print("B")
        
class C(A,B):
    def dispC(self):
        print("c")
c=C()
c.dispA()
c.dispB()
c.dispC()
print("====================")
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
        
class C(A):
    def dispC(self):
        print("c")
class D(B,C):
    def dispD(self):
        print("D")
d=D()
d.dispA()
d.dispB()
d.dispC()
d.dispD()
print("========================")
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30
cf=C()
print(cf.c)
print(cf.b)
print(cf.a)
print("====================")
class A:
    def dispA(self):
        print("A")
print(A.mro())
class B(A):
    def dispB(self):
        print("B")
print(B.mro())   
class C(B,A):
    def dispC(self):
        print("c")
print(C.mro())