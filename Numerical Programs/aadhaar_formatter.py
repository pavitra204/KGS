aadhaar = input("enter the number:")
first4  = aadhaar[:4]
middle4 = aadhaar[4:8]
last4   = aadhaar[8:]
print("First 4 digits :", first4)
print("Middle 4 digits:", middle4)
print("Last 4 digits:", last4)
print("Formatted:", f"{first4}-{middle4}-{last4}")
