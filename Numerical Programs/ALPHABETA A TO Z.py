n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            if j==1 or j==n-i:
                print(chr(64+j),end=" ") 
            else:
                print(chr(96+j),end=" ")
        if i%2==0:
            if j==1 or j==n-i:
                print(chr(96+j),end=" ")
            else:
                print(chr(64+j),end=" ")
    print()