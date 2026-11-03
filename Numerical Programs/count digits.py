def countDigit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
n=int(input("Enter a number: "))
res=countDigit(n)
print("The count of digits in", n, "is:", res)
