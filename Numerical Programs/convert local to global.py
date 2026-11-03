a=10
def fun1():
    global a
    a=100
    print(a)
    b=20
    print(b)
def fun2():
    a=1000
    print(a)
    b=30
    print(b)
print(a)
fun1()
fun2()
print(a)
print("\n==========================================")

def fun1():
    print("inside the KGS")
def add(x,y):
    z=x+y
    print(z)
print(fun1)
print(add)
fun1()
add(10,20)
ptr1=fun1
print(fun1)
ptr2=add
print(add)
ptr1()
ptr2(20,100)

print("\n=================================")
def fun1():
    print("inside the KGS")
def add(x,y):
    z=x+y
    print(z)
def display(ptr1,ptr2):
    ptr1()
    ptr2(10,46)
print(fun1)
print(add)
fun1()
add(10,20)
ptr3=fun1
print(fun1)
ptr4=add3
print(add)
ptr1()
ptr2(20,100)
display(ptr3,ptr4)
ptr3()
ptr4(10,38)