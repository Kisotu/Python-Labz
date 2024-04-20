#!/usr/bin/python3

# Department class

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, employee):
        self.employees.remove(employee)

    def printEmployee(self):
        print(f"Employees in {self.name} department: ")

        for emp in self.employees:
            print(emp.name)


# Employee Class

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department


    def __str__(str):
        return f"{self.name} from {self.department.name}"


# instantiate department

marketing = Department("Marketing")

engineering = Department("Engineering")


# create Employees
emp1 = Employee("Jake", engineering)
emp2 = Employee("Miss", marketing)

emp3 = Employee("Wanjiru", engineering)

# add employees to department

marketing.addEmployee(emp2)

engineering.addEmployee(emp1)
engineering.addEmployee(emp3)


# display employees
marketing.printEmployee()


# print engineering emps
engineering.printEmployee()

# Remove employee from engineering
engineering.removeEmployee(emp3)

print("**List after removing employee in engineering**")
engineering.printEmployee()
