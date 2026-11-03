def isPrime(n):
    countFact = 0
    for i in range(1, (n + 1)):
        if n % i == 0:
            countFact += 1
    return countFact == 2
num=int(input("Enter a number: "))
def countingcycles(n):
    i=1
    countcycles=0
    while i*i<=n:
        countcycles+=1
        i+=1
    return countcycles
def countPrimeFactors(num):
    count = 0
    for i in range(2, num + 1):
        if isPrime(i):
            count += 1
    return count
print("not prime number:")
for i in range(2, num + 1):
    if not isPrime(i):
        print(i, end=" ")
count=int(input("\nenter the count num:"))
series=1
print("the first",count,"not prime number are")
while count > 0:
    if not isPrime(series):
        print(series,end=" ")
        count=count-1
    series=series+1
count = countPrimeFactors(num)
print("\nCount of prime numbers till", num, "is:", count)
resCycles = countingcycles(num)
print("\nthe count of cycles taken to get the factors of", num, "is: ", resCycles)