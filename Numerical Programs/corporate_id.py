emp = input("Enter employee code: ")

company  = emp[:3]
branch   = emp[4:7]
tech     = emp[8:11]
emp_num  = emp[12:]

print("Company Code     :", company)
print("Branch           :", branch)
print("Technology       :", tech)
print("Employee Number  :", emp_num)
