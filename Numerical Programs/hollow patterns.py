print("hallow patters square")
n=int(input("enter the number:"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
print("hallow patters triangle")
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
print("right hallow triangle")
n=int(input("enter the number:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
print("right hallow pyramid")
n=int(input("enter the number:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
n=int(input("enter the number:"))
print("hallow inverted LHS triangle")
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        if i==1 or j==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
n=int(input("enter the number:"))
print("hallow inverted RHS tri angle")
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(n,i-1,-1):
        if i==1 or j==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================")
n=int(input("enter the number:"))
print("hallow lhs k patterns")
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        if i==1 or (i==(n*2)-1) or j==1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("===============================")        
n=int(input("enter the number:"))
print("hallow rhs k patterns")
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end=" ")
    for j in range(1,noc+1):
        if i==1 or (i==(n*2)-1) or j==1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("================================")
n=int(input("enter the number:"))
print("hallow inverted pyramid")
for i in range(1,n+1):
    for k in range(1,i,-1):
        print(" ",end=" ")     
    for j in range(n,1-1,-1):
        if i==1 or j==n or i==j:
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()
print("================================") 
n=int(input("enter the number:"))
print("hallow rhs sandglass patterns")
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if i==1 or (i==(n*2)-1) or j==1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
n=int(input("enter the number:"))
print("hallow pattern diamond")
noc=1
for i in range(1,(n*2)-1):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if i==1 or j==1 or i==(n*2)-1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc=-1

n = int(input("Enter num: "))
noc = 1
for i in range(1, (n * 2)):
    for k in range(n, noc, -1):
        print(" ", end="")
    for j in range(1, (noc + 1)):
        if j == noc or j == 1: 
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1