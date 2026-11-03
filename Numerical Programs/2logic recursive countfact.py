def Factor(n,i):
    if  i*i>n:
        return Factor
    if n%i==0:
        print(i,end=" ")
        if i!=(n//i):
            print(n//i,end=" ")
    return Factor(n,(i+1))
num=int(input("enter the number:"))
Factor(num,1)
#print("the factor of",num,"is",res)


def CountFactor(n,i,CountFact):
    if i*i>n:
        return CountFact
    if n%i==0:
        CountFact+=1
        if i!=(n//i):
            CountFact+=1
    return CountFactor(n,(i+1),CountFact)
num=int(input("\nenter the number:"))
res=CountFactor(num,1,0)
print("\nthe countfactor of",num,"is",res)