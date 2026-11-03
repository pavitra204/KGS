balance = 10000
PIN = 1234
print("      WELCOME TO KGS ATM")
print("Insert ATM Card")
card = 1
if card == 1:
    print("Card Inserted Successfully")

pin = int(input("Enter your 4-digit PIN: "))

if pin != PIN:
    print("Incorrect PIN. Please try again.")
    exit()

print("\nSelect Language")
print("1. English")
print("2. Hindi")
print("3. Kannada")
print("4. Telugu")

language = int(input("Enter your choice: "))

if language == 1:
    print("English Selected")
elif language == 2:
    print("Hindi Selected")
elif language == 3:
    print("Kannada Selected")
elif language == 4:
    print("Telugu Selected")
else:
    print("Invalid Language")
    exit()

print("\nSelect Transaction")
print("1. Withdraw")
print("2. Deposit")
print("3. Balance Enquiry")

choice = int(input("Enter your choice: "))

# Withdraw
if choice == 1:

    print("\nSelect Account Type")
    print("1. Savings")
    print("2. Current")

    account = int(input("Enter your choice: "))

    if account == 1:
        print("Savings Account")
    elif account == 2:
        print("Current Account")
    else:
        print("Invalid Account")
        exit()

    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance and amount % 100 == 0:

        balance -= amount

        print("\nProcessing...")
        print("Please Wait...")
        print("Collect Your Cash")

        ans = int(input("Do you want to see balance? (1.Yes 2.No): "))

        if ans == 1:
            print("Available Balance:", balance)

        print("\n--------- RECEIPT ---------")
        print("Transaction : Withdraw")
        print("Amount      :", amount)
        print("Balance     :", balance)
        print("---------------------------")

        print("Transaction Successful")
        print("Thank You")
        print("Visit Again")

    else:
        print("Insufficient Balance or Invalid Amount")

# Deposit
elif choice == 2:

    amount = int(input("Enter deposit amount: "))

    if amount % 100 == 0:
        balance += amount
        print("Deposit Successful")
        print("Available Balance:", balance)
    else:
        print("Invalid Amount")

# Balance Enquiry
elif choice == 3:
    print("Available Balance:", balance)

else:
    print("Invalid Transaction")