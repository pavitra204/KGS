def Factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

def countFactors(n):
    countFactors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            countFactors += 1
    return countFactors

num = int(input("Enter the number: "))
print("The factors of", num, "are:")
Factors(num)
res = countFactors(num)
print("\nThe count of factors of", num, "is:", res)