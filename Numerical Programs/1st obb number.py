def isEvenodd(n):
    return n % 2 == 0
count = int(input("Enter a number: "))
series = 1
print("The first", count, "Evennumbers are:")
while count > 0:
    if  not isEvenodd(series):
        print(series, end=" ")
        count -= 1  
    series += 1