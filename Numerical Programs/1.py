print("Welcome to my Hotel")
print("1. South Karnataka")
print("2. North Karnataka")
print("3. East Karnataka")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nSouth Karnataka Dishes")
    print("1. Roti")
    print("2. Rice")
    print("3. Dal")

    choose = int(input("Enter your dish number: "))

    if choose == 1:
        print("You selected: Roti")
    elif choose == 2:
        print("You selected: Rice")
    elif choose == 3:
        print("You selected: Dal")
    else:
        print("Invalid dish choice.")

elif choice == 2:
    print("\nNorth Karnataka Dishes")
    print("1. Mudde")
    print("2. Jolada Roti")
    print("3. Dal")

    choose = int(input("Enter your dish number: "))

    if choose == 1:
        print("You selected: Mudde")
    elif choose == 2:
        print("You selected: Jolada Roti")
    elif choose == 3:
        print("You selected: Dal")
    else:
        print("Invalid dish choice.")

elif choice == 3:
    print("\nEast Karnataka Dishes")
    print("1. Ragi Mudde")
    print("2. Rice")
    print("3. Sambar")

    choose = int(input("Enter your dish number: "))

    if choose == 1:
        print("You selected: Ragi Mudde")
    elif choose == 2:
        print("You selected: Rice")
    elif choose == 3:
        print("You selected: Sambar")
    else:
        print("Invalid dish choice.")

else:
    print("Invalid menu choice.")