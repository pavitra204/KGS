class Employee:
    company_name   = "KAIZENTRIX GLOBAL SOLUTIONS"
    employee_count = 0
    def __init__(self, employee_name, department):
        self.employee_name = employee_name
        self.department    = department
        Employee.employee_count += 1
    def generate_employee_id(self):
        employee_id = "EMP" + str(Employee.employee_count).zfill(3) + "-" + self.department[:3].upper()
        print("========================================")
        print("         EMPLOYEE ID GENERATED          ")
        print("========================================")
        print("Company Name:",Employee.company_name)
        print("Employee Name:",self.employee_name)
        print("Department:",self.department)
        print("Employee ID:",employee_id)
        print("Total Staff:",Employee.employee_count)
        print("========================================")

emp1 = Employee("Ravi Kumar",  "Development")
emp2 = Employee("Priya Singh", "Marketing")
emp3 = Employee("Arun Patel",  "Human Resource")
emp1.generate_employee_id()
emp2.generate_employee_id()
emp3.generate_employee_id()
