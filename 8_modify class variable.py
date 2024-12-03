class Employee:
    #Class variable
    company_name = "Gartner"

    def __init__(self,name,salary):
        #Instance variables
        self.name=name #attribute for employee name
        self.salary=salary #attribute for employee salary

    def display_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}\nCompany: {Employee.company_name}\n"

# Creating instances of Employee
emp1 = Employee("Ayush Kumar", 100000)
emp2 = Employee("Rounak Aggarwal", 95000)

# Displaying information for each employee
print(f"Details of Employee 1:\n{emp1.display_info()}")
print(f"Details of Employee 2:\n{emp2.display_info()}")

# Modifying class variable
Employee.company_name = "Infosys"

print("\nAfter changing the company name:\n")
print(f"Details of Employee 1:\n{emp1.display_info()}")
print(f"Details of Employee 2:\n{emp2.display_info()}")