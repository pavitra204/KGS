def is_countDigit(n):
    count=0
    while n > 0:
        n=n//10
        count=count+1
    return count
def is_ArmStrong(n):
    temp=n
    asn=0
    pow=is_countDigit(n)
    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
        
    if temp <0:
        n=n*-1
    return temp==asn
count=int(input("enter the count num:"))
series=1
print("the first",count,"ArmStrong numbers are")
while count > 0:
    if not is_ArmStrong(series):
        print(series,end=" ")
        count=count-1
    series=series+1