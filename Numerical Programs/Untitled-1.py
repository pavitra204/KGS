print("*")
print("==========================")
print()
print("hello")
print("world")
print("hello",end=" ")
print("world")
print("*")

n=int(input("enter the num:"))
for i in range(1,(n+1)):
    print("*")
print("==========================")    
    
n=int(input("enter the num:"))
for i in range(1,(n+1)):
    print("*",end=" ")
print("\n==========================")

n=int(input("enter the num:"))
#multiple rows
for i in range(1,(n+1)):
    #multiple cols
    for j in range(1,(n+1)):
        print("*",end=" ")
    print()
    
n=int(input("enter the num:"))
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print("*",end="")
    print()

n=int(input("enter the num:"))
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
    
n=int(input("enter the num:"))
for i in range(1,(n+1)):
    for j in range(n,i-1,-1):
        print("*",end="")
    print()