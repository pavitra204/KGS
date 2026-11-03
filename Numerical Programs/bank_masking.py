account = input("Enter account number: ")

masked = "*" * len(account[:-4]) + account[-4:]

print("Masked Account:", masked)
