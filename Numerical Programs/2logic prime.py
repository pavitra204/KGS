def is_Prime(n):
    countFactor=0
    i=1
    while i*i<=n:
        if n%i==0:
            countFactor+=1
            if i!=(n//i):
                countFactor+=1
        i+=1
    return countFactor==2
num=int(input("enter the numb :"))
if is_Prime(num):
    print(num,"\nis prime")
else:
    print(num,"\nis not a prime")