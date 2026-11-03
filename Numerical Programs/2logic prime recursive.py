def isPrime(n,i,CountFact):
    if i*i>n:
        return CountFact==2
    if n%i==0:
        CountFact+=1
        if i!=(n//i):
            CountFact+=1
    return isPrime(n,(i+1),CountFact)
num=int(input("\nenter 2the number:"))
if isPrime(num,1,0):
    print(num,"is prime")
else:
    print(num,"is not prime")
