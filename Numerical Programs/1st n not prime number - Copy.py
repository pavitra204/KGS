def is_prime(n):
    countFactor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            countFactor += 1
    return countFactor == 2
count=int(input("enter the count num:"))
series=1
print("the first",count,"prime number are")
while count > 0:
    if not is_prime(series):
        print(series,end=" ")
        count=count-1
    series=series+1