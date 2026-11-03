def countDigit(n,count):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
def is_ASN(n,pow,asn,temp):
    if n<=0:
        return asn==temp
    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
        return is_ASN(n,pow,asn,temp)
num=int(input("enter the number:"))
pow=countDigit(num,0)
if is_ASN(num,pow,0,num):
    print(num,"is a ASN")
else:
    print(num,"is not a ASN")