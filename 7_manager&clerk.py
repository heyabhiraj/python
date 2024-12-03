# Base class
class Employee:
    #Constructor to initialize attributes
    def __init__(self,name,emp_id):
        self.name=name #attribute for employee name
        self.emp_id=emp_id #attribute for employee id

    #Method to display the details of the Employee
    def display_info(self):
        return f"Name: {self.name}\nEmployee ID: {self.emp_id}"

# Derived class for Manager
class Manager(Employee):
    def __init__(self, name,emp_id,department):
        #calling the Base class (Employee) constructor
        super().__init__(name,emp_id)
        self.department=department #Initializing an additional attribute department

    #Method to display the details of the Manager
    def display_info(self):
        return f"{super().display_info()}\nDepartment: {self.department}\n"

# Derived class for Clerk
class Clerk(Employee):
    def __init__(self, name, emp_id, role):
        #calling the Base class (Employee) constructor
        super().__init__(name,emp_id)
        self.role=role #Initializing an additional attribute role

    #Method to display the details of the Clerk
    def display_info(self):
        return f"{super().display_info()}\nRole: {self.role}\n"

#creating object of the Derived Class: Manager and Clerk from Employee
manager=Manager("John Carley","GR_SD0237","Sales Department")
clerk=Clerk("Alex Washington","GR_MD0481","Data Entry")

#accessing methods to display details of Manager and Clerk
print(f"Details of Manager:\n{manager.display_info()}")
print(f"Details of Clerk:\n{clerk.display_info()}")
