def is_countDigit(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
def is_ASN(n):
    temp=n  
    asn=0
    pow=is_countDigit(n)
    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
    
    if temp<0:
        asn=asn*-1
    return temp==asn
num=int(input("enter the number:"))
if is_ASN(num):
    print(num," is ANS")
else:
    print(num,"is not ANS")

    
    