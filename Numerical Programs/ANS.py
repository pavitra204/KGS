def is_countDigit(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
def is_ASN(n):
    temp=n
    ans=0
    pow=is_countDigit(n)
    while n>0                                                                                                       :
        base=n%10
        ans=ans+(base**pow)
        n=n//10
    return temp==ans
num=int(input("enter the number:"))
if is_ASN(num):
    print(num," is ANS")
else:
    print(num,"is not ANS")

    
    